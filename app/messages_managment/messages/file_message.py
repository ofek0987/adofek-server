from __future__ import annotations

from dataclasses import dataclass

from app.enums.message_type import MessageType
from app.messages_managment.messages.base_message import BaseMessage


@dataclass
class FileMessage(BaseMessage):
    file_id: str

    @property
    def type(self) -> MessageType:
        return MessageType.FILE
