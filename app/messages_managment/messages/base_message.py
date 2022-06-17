from __future__ import annotations

import json
from abc import ABCMeta
from abc import abstractmethod
from dataclasses import dataclass
from datetime import datetime
from typing import TYPE_CHECKING

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
        dict_json = self._get_vars_dict_for_json()
        dict_json[consts.MESSAGE_JSON_TYPE_FIELD] = self.type.value
        return json.dumps(dict_json)

    def _get_vars_dict_for_json(self) -> dict:
        """Generate stringified dict from the class's properties."""
        return {
            key: str(value)
            for key, value in vars(self).items()
        }
