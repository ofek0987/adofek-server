from __future__ import annotations

from enum import Enum


class UserStatus(Enum):
    ONLINE = "online"
    DND = "dnd"
    OFFLINE = "offline"
