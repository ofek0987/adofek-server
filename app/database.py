from __future__ import annotations

from typing import Any

from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from app import config

engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine),
)
Base: Any = declarative_base()
Base.query = db_session.query_property()


def _clean_session_threads(application: Flask):
    """
    Clean db session for each thread.
    Check https://flask.palletsprojects.com/en/2.1.x/patterns/sqlalchemy/
    Args:
        application (Flask): The singelton flask application.
    """

    @application.teardown_appcontext
    def shutdown_session(exception: Exception = None):
        db_session.remove()


def init_db(application: Flask):
    import app.models  # noqa: F401

    _clean_session_threads(application)
    Base.metadata.create_all(bind=engine)
