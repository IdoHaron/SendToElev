from databases.data_map import MapDB
from pathlib import Path
from abc import ABC, abstractmethod


class TemplatesDB(MapDB, ABC):
    def __init__(self, path_to_template_db: Path):
        self._path = path_to_template_db
        self._load_db()

    @abstractmethod
    def get_path(self, template_name: str):
        raise NotImplementedError

    @abstractmethod
    def _load_db(self):
        raise NotImplementedError