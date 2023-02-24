from abc import ABC, abstractmethod
from typing import Callable

OnMessageReceive = Callable[[str], None]


class MessageManager:

    @property
    @abstractmethod
    def text_destination(self):
        raise NotImplemented

    @abstractmethod
    def get_new_messages(self):
        raise NotImplemented
