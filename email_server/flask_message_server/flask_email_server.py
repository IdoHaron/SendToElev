from typing import List
#TODO(Ido): learn how to minimaize outside exposure of modules __all__
from email_server.message_server import MessageServer
from server.flask_server.flask_server import FlaskServer
from flask import render_template, request, redirect
from input_pipelines.input_pipeline import InputPipeline
from utils.data_types.message import Message
from security_modules.security_module import SecurityModule
from utils.decorators import singleton
from security_modules.security_module import SecurityModule
from flask_login import LoginManager, login_user, login_required
from pathlib import Path
from importlib import reload
from __future__ import annotations

#TODO(ido): should figure-out how 

@singleton
class FlaskMessageServer(FlaskServer, MessageServer):
    server_instace:FlaskMessageServer = None

    def __init__(self, message_manager: InputPipeline, security_module: SecurityModule,
                 wanted_module_name: str = __name__,
                 host: str = "127.0.0.1", port: int = 3000):
        FlaskServer.__init__(self, wanted_module_name=wanted_module_name, path_to_templates=Path("website_pages"))
        MessageServer.__init__(self, message_manager, security_module)
        FlaskMessageServer.server_instace = self
        self.login_manager = LoginManager()
        FlaskServer._SERVER.run(host=host, port=port)
        reload(FlaskMessageServer)
        self.login_manager.init_app(self._SERVER)


    @staticmethod
    @FlaskServer._SERVER.route("/<board_id>/<security_details>")
    def client_fetch_new_messages(board_id: str, security_details: str) -> str:
        #TODO(ido): move security details from 
        if not FlaskMessageServer.server_instace._security_module.verify_client(board_id, security_details):
            return ''
        print("here")
        return FlaskMessageServer.server_instace._message_manager.get_new_messages(board_id)

    @staticmethod
    @FlaskServer._SERVER.route("/")
    def load_login_page():
        return render_template("login_page.html")

    @staticmethod
    @FlaskServer._SERVER.route("/login", methods=["POST"])
    def login_details():
        #TODO(Ido): think about uniting with the basic index route.
        print("here")
        username, password = request.form["username"], request.form["password"]
        if FlaskMessageServer.server_instance._security_module.verify_client(username, password):
            login_user(username)
        #TODO(ido): add check for url safe for  redirection
        return redirect("/message_form_window")

    @staticmethod
    @server_instace.login_manager.user_loader
    def load_user(user_id):
        return FlaskMessageServer.server_instace._security_module.connected_client(user_id)

    
    @staticmethod
    @FlaskServer._SERVER.route("/message_form_window")
    def message_form_window():
        #TODO(Ido): might be worth to unite with the post location
        #TODO(Ido): read about serving with images, think about how to make the templates dynamic so other templates could be showed.
        return render_template("message_form.html")

    @staticmethod
    @FlaskServer._SERVER.route("/image", methods=["POST"])
    @login_required
    def new_image():
        board_name, image_in_code = request.form["board_name"], request.form["image"]

    