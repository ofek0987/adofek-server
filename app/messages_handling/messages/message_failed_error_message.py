from __future__ import annotations

from dataclasses import dataclass, field

from dataclasses_json import config
from marshmallow import fields

from app.enums.message_type import MessageType
from app.messages_handling.messages.error_message import ErrorMessage


@dataclass
class MessageFailedErrorMessage(ErrorMessage):
    """Will be sent to the sender of a failed message."""

    failed_message_id: str = field(
        metadata=config(
            mm_field=fields.String(),
        ),
    )

    @property
    def type(self) -> MessageType:
        return MessageType.MESSAGE_FAIL
