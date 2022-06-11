from __future__ import annotations

from enum import Enum


class MessageType(Enum):
    """Message types to be used for messages at json form."""
    TEXT = 'text'
    FILE = 'file'
    IMAGE = 'image'
