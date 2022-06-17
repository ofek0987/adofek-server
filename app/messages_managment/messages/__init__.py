from __future__ import annotations

import json

from .message_failed_error_message import MessageFailedErrorMessage
from .message_sent_message import MessageSentMessage
from app import consts
from app.enums.message_type import MessageType
from app.messages_managment.messages.base_message import BaseMessage
from app.messages_managment.messages.error_message import ErrorMessage
from app.messages_managment.messages.file_message import FileMessage
from app.messages_managment.messages.image_message import ImageMessage
from app.messages_managment.messages.text_message import TextMessage


def _get_message_type(json_data: str):
    return MessageType(
        json.loads(
            json_data,
        )[consts.MESSAGE_JSON_TYPE_FIELD],
    )


def resolve_json_to_message(json_data: str) -> BaseMessage:
    """
    Create message object based on its json representation.
    Assumes the json data is valid.
    :param json_data: The json data to resolve.
    :return: Message object
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
    message_type = _get_message_type(json_data)
    return message_type_to_message_class_resolver[message_type] \
        .from_json(json_data)
