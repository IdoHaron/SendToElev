from os import system, getcwd, chdir
from pathlib import Path
from email_server.flask_message_server.flask_email_server import FlaskMessageServer
from security_modules.everything_passes import EverythingPasses
from input_pipelines.dummy_input_pipeline import DummyInput

FlaskMessageServer(DummyInput(), EverythingPasses())

#TODO(Ido): should implement an elevator side test, for the fetching ETC.
