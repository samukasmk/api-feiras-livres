#!/usr/bin/env python
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from app import app, db, models

manager = Manager(app)

# command: runserver
runserver = Server(host="0.0.0.0", port=8080)
manager.add_command("runserver", runserver)

# command: db *
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

# command: shell
@manager.shell
def make_shell_context():
    return dict(app=app, db=db, models=models)

# command: hello
@manager.command
def hello():
    print("hello")

if __name__ == "__main__":
    manager.run()



# import os
# from flask.ext.script import Manager
# from flask.ext.migrate import Migrate, MigrateCommand
#
# from app import app, db
#
# app.config.from_object(os.environ['APP_SETTINGS'])
#
# migrate = Migrate(app, db)
# manager = Manager(app)
#
# manager.add_command('db', MigrateCommand)
#
# if __name__ == '__main__':
#     manager.run()
