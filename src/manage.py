#!/usr/bin/env python
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from app import create_app, models
from app.database import db
from helpers.csv_reader import iter_csv_file

app = create_app(__name__)
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

# command: populate_from_csv
@manager.command
def populate_from_csv(csv_file):
    for row_dict in iter_csv_file(csv_file):
        _feira_obj = models.FeiraLivre(
            numero=row_dict.pop('numero').split('.')[0], **row_dict)
        db.session.add(_feira_obj)
    db.session.commit()


if __name__ == "__main__":
    manager.run()
