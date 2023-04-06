from typing import List

from databases.elevator_board.elevator_boards_table import ElevatorBoardsTable
from pathlib import Path
from json import load

from databases.elevator_board.elivator_board_entry import ElevatorBoardEntry
from utils.data_types import UserId
from exceptions.database_error.exceptions import ValueNotFound


class JsonElevatorBoardsTable(ElevatorBoardsTable):
    def __init__(self, path_to_json:Path):
        super().__init__(path_to_json)
        self.json_content:dict = {}
        self.connect_to_db(self._database_path)

    def connect_to_db(self, database_path:Path):
        with self._database_path.open("r") as f:
            self.json_content = load(f)

    def value_in_database(self, value_in_db:str):
        print(self.json_content)
        return value_in_db in self.json_content

    def fetch_info_by_id(self, user_id: UserId) -> List[ElevatorBoardEntry]:
        print(user_id)
        if not self.value_in_database(user_id):
            raise ValueNotFound
        boards_entries = []
        for board in self.json_content[user_id]:
            board_name = board["name"]
            boards_entries.append(ElevatorBoardEntry(user_id, board_name))
        return boards_entries