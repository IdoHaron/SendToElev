from flask import Flask
from server.server_interface import Server
from server.utils import ServerState


class FlaskServer(Server):
    _SERVER: Flask = None
    def __init__(self, wanted_module_name: str = __name__):
        self.wanted_module_name = wanted_module_name
        self.server_state = ServerState.DOWN
        self.server_up()

    def start_server(self):
        return self.server_up()

    def server_up(self):
        if self.server_state is not ServerState.UP:
            return
        FlaskServer._SERVER = Flask(self.wanted_module_name)
        self.server_state = ServerState.UP
        #should figure out if there is a way to start the server purely from python

    def server_sleep(self):
        if self.server_state is ServerState.SLEEP:
            return
        self.server_state = ServerState.SLEEP

    def server_down(self):
        if self.server_state is ServerState.DOWN:
            return
        self.server_state = ServerState.DOWN

    def change_server_state(self, wanted_server_state:ServerState):
        if wanted_server_state is ServerState.UP:
            return self.start_server()
        if wanted_server_state is ServerState.SLEEP and wanted_server_state is ServerState.DOWN:
            self.start_server()
            return self.server_sleep()
        if wanted_server_state is ServerState.SLEEP:
            return self.server_sleep()
        if wanted_server_state is ServerState.DOWN:
            return self.server_down()

