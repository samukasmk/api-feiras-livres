import os
import pytest
from flask_migrate import upgrade, Migrate
from app import create_app
from app.database import db as _db

SRC_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
TESTDB_PATH = os.path.join(SRC_DIR, 'tests/db/testing.db')
TESTDB_URI = 'sqlite:///' + TESTDB_PATH
MIGRATIONS_PATH = os.path.join(SRC_DIR, 'migrations')


@pytest.fixture(scope='session')
def app(request):
    # remove existing database file
    if os.path.exists(TESTDB_PATH):
        os.unlink(TESTDB_PATH)

    # define override settings for flask app
    settings_override = {
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': TESTDB_URI}

    # build app object
    app = create_app(__name__, settings_override)

    # establish an application context before running the tests.
    # http://flask.pocoo.org/docs/0.12/api/#flask.Flask.test_request_context
    with app.test_request_context() as ctx:
        # ensure to drop all sqlite data
        _db.drop_all()
        # define Migrations config obj
        migrate = Migrate(app, _db)
        # run migration scripts in database with upgrade command
        upgrade(directory=MIGRATIONS_PATH)
        # push app context
        ctx.push()

    # define teardown actions for end tests
    def teardown():
        # drop all sqlite data
        _db.drop_all()
        # remove temporary database
        os.unlink(TESTDB_PATH)
        # pop app context
        ctx.pop()

    # attach teardown actions
    request.addfinalizer(teardown)

    # return configurated app for tests
    return app
