from flask import Flask
from flask_restful import Api
from .logger import set_access_log, set_error_log


def create_app(name, settings_override={}):
    # Define the WSGI application object
    app = Flask(name)

    # Load Configurations
    app.config.from_object('config')
    app.config.update(settings_override)

    # Set access.log logging handler
    set_access_log(app)
    set_error_log(app)

    # Initialize database for app:
    from app.database import db
    db.init_app(app)

    # Build flask_restful api obj
    from app.api import feira_livre_api
    api = Api(app)

    # Attach Blueprint api urls
    app.register_blueprint(feira_livre_api)

    return app
