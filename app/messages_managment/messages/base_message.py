from __future__ import annotations

from abc import ABCMeta
from abc import abstractmethod
from dataclasses import dataclass
from datetime import datetime


@dataclass  # type: ignore
class BaseMessage(metaclass=ABCMeta):
    message_id: str
    from_user: str
    to_user: str
    sent_timestamp: datetime

    @abstractmethod
    def to_json(self) -> str:
        ...
