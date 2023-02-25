from os import system, getcwd, chdir
from pathlib import Path
from email_server.flask_message_server.flask_email_server import FlaskMessageServer
from security_modules.everything_passes import EverythingPasses
from message_managers.dummy_message_manager import DummyMessageManager

FlaskMessageServer(DummyMessageManager(), EverythingPasses())


