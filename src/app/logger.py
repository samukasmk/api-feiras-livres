import os
import logging
from logging.handlers import RotatingFileHandler


# Set access.log logging handler, level and format
def set_access_log(app):
    logger = logging.getLogger('werkzeug')
    accesslog_handler = RotatingFileHandler(
        os.path.join(app.config['LOGGING_FOLDER'], 'api_feira_livre-access.log'),
        maxBytes=app.config['LOGGING_ROTATE_SIZE'] * 1024 * 1024,
        backupCount=app.config['LOGGING_ROTATE_COUNT'])
    logger.addHandler(accesslog_handler)


# Set error.log logging handler, level and format
def set_error_log(app):
    errorlog_handler = RotatingFileHandler(
        os.path.join(app.config['LOGGING_FOLDER'], 'api_feira_livre-error.log'),
        maxBytes=app.config['LOGGING_ROTATE_SIZE'] * 1024 * 1024,
        backupCount=app.config['LOGGING_ROTATE_COUNT'])
    errorlog_handler.setLevel(app.config['LOGGING_LEVEL'])
    if 'LOGGING_FORMAT' in app.config:
        formatter = logging.Formatter(app.config['LOGGING_FORMAT'])
        errorlog_handler.setFormatter(formatter)
    app.logger.addHandler(errorlog_handler)
