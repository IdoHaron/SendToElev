from abc import abstractmethod
from utils.data_types.message import Message
from message_managers.message_manager import MessageManager
from typing import List


class MessageServer:
    __slots__ = ["_message_manager"]
    @abstractmethod
    def __init__(self, message_manger:MessageManager):
        self._message_manager = message_manger

    @abstractmethod
    def client_fetch_emails(self, board_id: str) -> List[Message]:
        raise NotImplementedError
