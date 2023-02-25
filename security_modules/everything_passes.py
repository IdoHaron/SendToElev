from security_modules.security_module import SecurityModule


class EverythingPasses(SecurityModule):
    def verify_client(self, client_id: str, client_security_details) -> bool:
        return True
