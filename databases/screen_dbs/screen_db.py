from databases.data_map import MapDB
class ScreenDB:
    def __init__(self,current_db_state:MapDB):
        self._current_db_state = current_db_state

    def legal_screen_id(self, screen_id) -> bool:
        return screen_id in self._current_db_state.__dict__().keys()