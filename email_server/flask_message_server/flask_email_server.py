from typing import List

from email_server.message_server import MessageServer
from server.flask_server.flask_server import FlaskServer
from message_managers.message_manager import MessageManager
from utils.data_types.message import Message


class FlaskMessageServer(FlaskServer, MessageServer):

    def __init__(self, message_manager: MessageManager, wanted_module_name: str = __name__):
        FlaskServer.__init__(self, wanted_module_name=wanted_module_name)
        MessageServer.__init__(self, message_manager)


