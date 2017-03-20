import os
import logging

# Define the application directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Statement for enabling the development environment
DEBUG = False

# Logging settings
LOGGING_FOLDER = '../logs'
LOGGING_LEVEL = logging.DEBUG
LOGGING_ROTATE_SIZE = 25 # IN MB
LOGGING_ROTATE_COUNT = 3
LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

# Define the database uri 'dialect+driver://username:password@host:port/database'
# http://flask-sqlalchemy.pocoo.org/2.1/config/?highlight=mysql#connection-uri-format

# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'api_feira_livre.db')
SQLALCHEMY_DATABASE_URI = 'mysql://root:toor@127.0.0.1/api_feira_livre'
SQLALCHEMY_POOL_SIZE = 5
SQLALCHEMY_POOL_TIMEOUT = 10
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = "dc176485cef85dd716af5308cb70df01"

# Secret key for signing cookies
SECRET_KEY = "9bc9267f53120664368ffb94d2f392d3"

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
# THREADS_PER_PAGE = 2
