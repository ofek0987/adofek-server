from __future__ import annotations

import json
from dataclasses import dataclass

from app import consts
from app.enums.message_type import MessageType
from app.messages_managment.messages.base_message import BaseMessage


@dataclass
class TextMessage(BaseMessage):
    """Ordinary text message sent in the chat."""
    text: str

    def to_json(self) -> str:
        future_json = {
            str(key): str(value)
            for key, value in vars(self).items()
        }
        future_json[consts.MESSAGE_JSON_TYPE_FIELD] = MessageType.TEXT.value
        return json.dumps(future_json)
