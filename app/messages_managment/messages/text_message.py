from __future__ import annotations

from dataclasses import dataclass

from app.enums.message_type import MessageType
from app.messages_managment.messages.base_message import BaseMessage


@dataclass
class TextMessage(BaseMessage):
    """Ordinary text message."""

    text: str

    @property
    def type(self) -> MessageType:
        return MessageType.TEXT
