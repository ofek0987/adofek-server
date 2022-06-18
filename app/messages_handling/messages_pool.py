from __future__ import annotations

import bisect
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.messages_handling.messages.base_message import BaseMessage


class MessagesPool:
    """Stores all the received messages in memory."""

    def __init__(self):
        self._messages_pool: dict[str, list[BaseMessage]] = {}

    def push_message(self, message: BaseMessage):
        """Add a message to the message pool."""
        if message.to_user in self._messages_pool.keys():
            bisect.insort(self._messages_pool[message.to_user], message)
        else:
            self._messages_pool[message.to_user] = [message]

    def pull_messages_assigned_to_user(self, user: str) -> list[BaseMessage]:
        """
        Get all the messages assigned to a user
        and remove them from the messages pool.
        :param user: The username of the user
                     that the message should be assigned to.
        :return: List of all the relevant messages
                 sorted by their sent timestamp.
        """
        return self._messages_pool.pop(user, [])
