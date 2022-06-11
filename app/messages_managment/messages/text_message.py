from __future__ import annotations

from dataclasses import dataclass

from app.messages_managment.messages.base_message import BaseMessage


@dataclass
class TextMessage(BaseMessage):
    text: str

    def to_json(self) -> str:
        pass
