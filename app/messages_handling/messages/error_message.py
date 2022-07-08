from __future__ import annotations

from dataclasses import dataclass, field

from dataclasses_json import config
from marshmallow import fields

from app.enums.message_type import MessageType
from app.messages_handling.messages.base_message import BaseMessage


@dataclass
class ErrorMessage(BaseMessage):
    reason: str = field(
        metadata=config(
            mm_field=fields.String(),
        ),
    )
    status_code: int = field(
        metadata=config(
            mm_field=fields.Integer(),
        ),
    )

    @property
    def type(self) -> MessageType:
        return MessageType.ERROR
