from abc import ABC, abstractmethod
from typing import Callable

OnMessageReceive = Callable[[str], None]


class InputPipeline:
    __slots__ = ["_on_message_receive"]

    def __init__(self, on_message_receive: OnMessageReceive):
        self._on_message_receive = on_message_receive

    @abstractmethod
    @property
    def text_destination(self):
        raise NotImplemented

    @abstractmethod
    def get_new_messages(self):
        raise NotImplemented
