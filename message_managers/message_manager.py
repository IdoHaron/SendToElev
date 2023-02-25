from abc import ABC, abstractmethod
from typing import Callable

OnMessageReceive = Callable[[str], None]


class MessageManager:
    @property
    @abstractmethod
    def text_destination(self):
        raise NotImplementedError

    @abstractmethod
    def get_new_messages(self, client_id:str):
        raise NotImplementedError

