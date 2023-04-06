from pathlib import Path
from abc import ABC, abstractmethod


class MapDB(ABC):
    @abstractmethod
    def __dict__(self)->dict:
        raise NotImplementedError
