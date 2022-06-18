from __future__ import annotations

from dataclasses_json.core import Json

from .message_failed_error_message import MessageFailedErrorMessage
from .message_sent_message import MessageSentMessage
from app import consts
from app.enums.message_type import MessageType
from app.exceptions.validation_error import ValidationError
from app.messages_managment.messages.base_message import BaseMessage
from app.messages_managment.messages.error_message import ErrorMessage
from app.messages_managment.messages.file_message import FileMessage
from app.messages_managment.messages.image_message import ImageMessage
from app.messages_managment.messages.text_message import TextMessage


def resolve_json_to_message(json_data: Json) -> BaseMessage:
    """
    Create message object based on its json representation.
    :param json_data: The json data to resolve.
    :return: Message object
    :raises ValidationError: If the given json is invalid.
    """
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
    try:
        message_type = MessageType(json_data[consts.MESSAGE_JSON_TYPE_FIELD])
        return message_type_to_message_class_resolver[message_type] \
            .from_dict(json_data)
    except (KeyError, ValueError):
        raise ValidationError(f'{json_data} is not a valid message.')
