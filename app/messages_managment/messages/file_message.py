from dataclasses import dataclass

from app.messages_managment.messages.base_message import BaseMessage


@dataclass
class FileMessage(BaseMessage):
    file_id: str

    def to_json(self) -> str:
        pass
