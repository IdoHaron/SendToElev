from abc import abstractmethod


class SecurityModule:
    @abstractmethod
    def verify_client(self, client_id: str, client_security_details) -> bool:
        raise NotImplementedError
