from __future__ import annotations

from sqlalchemy import Column, String
from werkzeug.security import check_password_hash, generate_password_hash

from app import consts
from app.database import Base


class User(Base):
    __tablename__ = consts.USERS_TABLE_NAME

    username = Column(String(consts.MAX_USERNAME_LENGTH), primary_key=True)
    password_hash = Column(String(consts.PASSWORD_HASH_MAX_LENGTH))
    status = Column(String(consts.USER_STATUS_MAX_LENGTH))

    def set_password(self, password: str):
        """Encrypt the password and save it as a property."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        """Checks if a given raw password matches the
        encrypted password saved in the database."""
        return check_password_hash(self.password_hash, password)  # type: ignore
