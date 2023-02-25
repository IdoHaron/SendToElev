from message_managers.message_manager import MessageManager


class DummyMessageManager(MessageManager):
    text_destination = ""

    def get_new_messages(self, client_id: str):
        return "dummy message"
