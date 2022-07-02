from __future__ import annotations

import typing
from abc import ABCMeta, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime

from dataclasses_json import DataClassJsonMixin, config
from marshmallow import fields

if typing.TYPE_CHECKING:
    from app.enums.message_type import MessageType


@dataclass  # type: ignore
class BaseMessage(DataClassJsonMixin, metaclass=ABCMeta):
    message_id: str = field(
        metadata=config(
            mm_field=fields.String(),
        ),
    )
    from_user: str = field(
        metadata=config(
            mm_field=fields.String(),
        ),
    )
    to_user: str = field(
        metadata=config(
            mm_field=fields.String(),
        ),
    )
    sent_timestamp: datetime = field(
        metadata=config(
            mm_field=fields.DateTime(format="iso"),
            encoder=datetime.isoformat,
            decoder=datetime.fromisoformat,
        ),
    )

    @property
    @abstractmethod
    def type(self) -> MessageType:
        """Message type in enum representation."""
        ...

    def __lt__(self, other: BaseMessage):
        return self.sent_timestamp < other.sent_timestamp
