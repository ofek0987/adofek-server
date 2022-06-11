from abc import ABC, abstractmethod
from datetime import datetime
from dataclasses import dataclass


@dataclass
class BaseMessage(ABC):
    message_id: str
    from_user: str
    to_user: str
    sent_timestamp: datetime

    @abstractmethod
    def to_json(self) -> str:
        ...
