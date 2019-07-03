


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from.config import BaseConfiguration as config_class

app = Flask(__name__)
app.config.from_object(config_class)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from . import models
from . import routes

if __name__ == '__main__':
    app.run(host='localhost', port=5000)