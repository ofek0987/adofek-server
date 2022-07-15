import json

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app import consts
from app.filebp.views import file_blueprint
from app.messagebp.views import messages_blueprint
from app.userbp.views import user_blueprint

db = SQLAlchemy()


def create_app() -> Flask:
    application = Flask(__name__)
    configure_app(application)
    init_db(application)
    init_blueprints(application)
    return application


def configure_app(application: Flask):
    application.config.from_file(consts.CONFIG_FILE, load=json.load)  # type: ignore


def init_blueprints(application: Flask):
    application.register_blueprint(file_blueprint)
    application.register_blueprint(messages_blueprint)
    application.register_blueprint(user_blueprint)


def init_db(application: Flask):
    import app.models  # noqa F401

    db.init_app(application)

    with application.app_context():
        db.create_all()
