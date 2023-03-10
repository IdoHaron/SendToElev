from abc import abstractmethod
from typing import Union


class SecurityModule:
    @abstractmethod
    def verify_client(self, client_id: str, client_security_details) -> bool:
        raise NotImplementedError

    @abstractmethod
    def connected_client(self, client_id:str)->Union[None, ]:
        raise NotImplementedError