from __future__ import annotations

from app.enums.message_type import MessageType
from app.messages_handling.messages.file_message import FileMessage


class ImageMessage(FileMessage):

    @property
    def type(self) -> MessageType:
        return MessageType.IMAGE
