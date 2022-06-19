from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field

from dataclasses_json import config
from marshmallow import fields

from app.enums.message_type import MessageType
from app.messages_handling.messages.base_message import BaseMessage


@dataclass
class TextMessage(BaseMessage):
    """Ordinary text message."""

    text: str = field(
        metadata=config(
            mm_field=fields.String(),
        ),
    )

    @property
    def type(self) -> MessageType:
        return MessageType.TEXT
