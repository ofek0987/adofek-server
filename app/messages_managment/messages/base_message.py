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
        """Represent a message in json form.
        Used for sending/receiving messages."""
        ...

    def _get_vars_dict_for_json(self) -> dict:
        """Generate stringified dict from the class's properties."""
        return {
            str(key): str(value)
            for key, value in vars(self).items()
        }
