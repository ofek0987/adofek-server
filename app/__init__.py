from flask import Flask

from app import database
from app.filebp.views import file_blueprint
from app.messagebp.views import messages_blueprint
from app.userbp.views import user_blueprint


def create_app():
    application = Flask(__name__)
    database.init_db(application)
    application.register_blueprint(file_blueprint)
    application.register_blueprint(messages_blueprint)
    application.register_blueprint(user_blueprint)
    return application
