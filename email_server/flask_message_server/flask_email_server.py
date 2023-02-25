from typing import List

from email_server.message_server import MessageServer
from server.flask_server.flask_server import FlaskServer
from message_managers.message_manager import MessageManager
from utils.data_types.message import Message
from security_modules.security_module import SecurityModule
from utils.decorators import singleton


class FlaskMessageServer(FlaskServer, MessageServer):
    server_instace = None

    def __init__(self, message_manager: MessageManager, security_module: SecurityModule,
                 wanted_module_name: str = __name__,
                 host: str = "127.0.0.1", port: int = 3000):
        FlaskServer.__init__(self, wanted_module_name=wanted_module_name)
        MessageServer.__init__(self, message_manager, security_module)
        FlaskMessageServer.server_instace = self
        FlaskServer._SERVER.run(host=host, port=port)

    @staticmethod
    @FlaskServer._SERVER.route("/<board_id>/<security_details>")
    def client_fetch_new_messages(board_id: str, security_details: str) -> str:
        if not FlaskMessageServer.server_instace._security_module.verify_client(board_id, security_details):
            return ''
        print("here")
        return FlaskMessageServer.server_instace._message_manager.get_new_messages(board_id)
