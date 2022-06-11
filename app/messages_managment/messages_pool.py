from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.messages_managment.messages.base_message import BaseMessage


class MessagesPool:
    def push(self, message: BaseMessage):
        ...

    def pull(self, message_id: str) -> BaseMessage:
        ...
