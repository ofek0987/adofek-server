from __future__ import annotations

from typing import Any

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

from app import config

engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine),
)
Base: Any = declarative_base()
Base.query = db_session.query_property()


def init_db():
    import app.models  # noqa: F401

    Base.metadata.create_all(bind=engine)
