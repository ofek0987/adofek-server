from __future__ import annotations

from dataclasses import dataclass, field

from dataclasses_json import config
from marshmallow import fields

from app.enums.message_type import MessageType
from app.messages_handling.messages.base_message import BaseMessage


@dataclass
class MessageSentMessage(BaseMessage):
    """Will be sent to a sender of a successfully sent message."""

    sent_message_id: str = field(
        metadata=config(
            mm_field=fields.String(),
        ),
    )

    @property
    def type(self) -> MessageType:
        return MessageType.MESSAGE_SENT
