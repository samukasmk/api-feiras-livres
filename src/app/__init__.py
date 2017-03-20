from flask import Flask, Blueprint, render_template
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from .logger import set_access_log, set_error_log

# Define the WSGI application object
app = Flask(__name__)

# Load Configurations
app.config.from_object('config')

# Set access.log logging handler
set_access_log(app)
set_error_log(app)

# Define the database object which is imported by modules and controllers
db = SQLAlchemy(app)
# Build the database:
db.create_all()

# Build flask_restful api obj
from app.api import feira_livre_api
api = Api(app)

# Attach Blueprint api urls
app.register_blueprint(feira_livre_api)
