from __future__ import annotations

import typing
from abc import ABCMeta
from abc import abstractmethod
from dataclasses import dataclass
from datetime import datetime

from dataclasses_json import DataClassJsonMixin

from app import consts
from app.types import JsonDict

if typing.TYPE_CHECKING:
    from app.enums.message_type import MessageType


@dataclass  # type: ignore
class BaseMessage(DataClassJsonMixin, metaclass=ABCMeta):
    message_id: str
    from_user: str
    to_user: str
    sent_timestamp: datetime

    @property
    @abstractmethod
    def type(self) -> MessageType:
        """Message type in enum representation."""
        ...

    def to_dict(self, encode_json: bool = False) -> JsonDict:
        result = super().to_dict(encode_json)
        result[consts.MESSAGE_JSON_TYPE_FIELD] = self.type.value
        return result

    @classmethod
    def from_dict(
            cls,
            kvs: JsonDict,
            *,
            infer_missing: bool = False,
    ) -> BaseMessage:
        kvs.pop(consts.MESSAGE_JSON_TYPE_FIELD)
        return super().from_dict(  # type: ignore
            kvs=kvs,
            infer_missing=infer_missing,
        )

    def __lt__(self, other: BaseMessage):
        return self.sent_timestamp < other.sent_timestamp
