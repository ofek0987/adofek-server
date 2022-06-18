from __future__ import annotations

import json
from abc import ABCMeta
from abc import abstractmethod
from dataclasses import dataclass
from datetime import datetime
from typing import TYPE_CHECKING

import dateutil.parser

from app import consts

if TYPE_CHECKING:
    from app.enums.message_type import MessageType


@dataclass  # type: ignore
class BaseMessage(metaclass=ABCMeta):
    message_id: str
    from_user: str
    to_user: str
    sent_timestamp: datetime

    @property
    @abstractmethod
    def type(self) -> MessageType:
        """Message type in enum representation."""
        ...

    def to_json(self) -> str:
        """Represent a message in json form.
        Used for sending/receiving messages."""
        dict_json = vars(self)
        dict_json[consts.MESSAGE_JSON_TYPE_FIELD] = self.type.value
        return json.dumps(dict_json, default=str)

    @classmethod
    def from_json(cls, json_data: str) -> BaseMessage:
        """
        Create a message object based on its json representation.
        The json data assumes to be valid and to match the message type.
        :param json_data: The data to create the message object by.
        :return: Message object.
        """
        data = json.loads(json_data)
        data.pop(consts.MESSAGE_JSON_TYPE_FIELD)
        data[consts.MESSAGE_SENT_TIMESTAMP_FILED] = dateutil.parser.parse(
            data[consts.MESSAGE_SENT_TIMESTAMP_FILED],
        )
        return cls(**data)

    def __lt__(self, other: BaseMessage):
        return self.sent_timestamp < other.sent_timestamp
