from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import os

from project import app

app.config.from_object('config.DevelopmentConfig')

migrate = Migrate(app)
manager = Manager(app)

if __name__ == '__main__':
    manager.run(debug=True)