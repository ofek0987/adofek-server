from __future__ import annotations

from .message_failed_error_message import MessageFailedErrorMessage
from .message_sent_message import MessageSentMessage
from app.enums.message_type import MessageType
from app.messages_handling.messages.base_message import BaseMessage
from app.messages_handling.messages.error_message import ErrorMessage
from app.messages_handling.messages.file_message import FileMessage
from app.messages_handling.messages.image_message import ImageMessage
from app.messages_handling.messages.text_message import TextMessage


def get_message_cls_by_type(message_type: MessageType) -> type[BaseMessage]:
    """Get message class by message type enum."""
    message_type_to_message_class_resolver: dict[
        MessageType,
        type[BaseMessage],
    ] = {
        MessageType.IMAGE: ImageMessage,
        MessageType.FILE: FileMessage,
        MessageType.TEXT: TextMessage,
        MessageType.ERROR: ErrorMessage,
        MessageType.MESSAGE_FAIL: MessageFailedErrorMessage,
        MessageType.MESSAGE_SENT: MessageSentMessage,
    }
    return message_type_to_message_class_resolver[message_type]
