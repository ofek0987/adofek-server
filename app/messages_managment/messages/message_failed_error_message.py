from __future__ import annotations

from dataclasses import dataclass

from app.enums.message_type import MessageType
from app.messages_managment.messages.error_message import ErrorMessage


@dataclass
class MessageFailedErrorMessage(ErrorMessage):
    """Will be sent to the sender of a failed message."""
    failed_message_id: str

    @property
    def type(self) -> MessageType:
        return MessageType.MESSAGE_FAIL
