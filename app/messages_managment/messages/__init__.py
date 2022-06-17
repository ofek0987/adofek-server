from __future__ import annotations

import json

from app import consts
from app.enums.message_type import MessageType
from app.messages_managment.messages.base_message import BaseMessage
from app.messages_managment.messages.file_message import FileMessage
from app.messages_managment.messages.image_message import ImageMessage
from app.messages_managment.messages.text_message import TextMessage


def resolve_json_to_message(json_data: str) -> BaseMessage:
    """
    Create message object based on its json representation.
    Assumes the json data is valid.
    :param json_data: The json data to resolve.
    :return: Message object
    """
    message_type_to_message_class_resolver = {
        MessageType.IMAGE: ImageMessage,
        MessageType.FILE: FileMessage,
        MessageType.TEXT: TextMessage,
    }
    message_type = MessageType(
        json.loads(
            json_data,
        )[consts.MESSAGE_JSON_TYPE_FIELD],
    )
    return message_type_to_message_class_resolver[message_type]\
        .from_json(json_data)
