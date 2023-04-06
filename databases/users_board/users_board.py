from abc import ABC
from pathlib import Path
from typing import List

from databases.general_user_based_db import GeneralUserDBEntry
from utils.data_types import UserId
from databases.users_board.user import User


class UsersBoard(GeneralUserDBEntry, ABC):
    pass