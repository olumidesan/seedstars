
# Import flask as the main web framework
# flask_sqlalchemy as the database ORM
# flask migrate for database version control
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Import the configuration class
from.config import BaseConfiguration as config_class

app = Flask(__name__)
app.config.from_object(config_class)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Register the routes and models with the application
from . import models
from . import routes

if __name__ == '__main__':
    # Run the server
    app.run(host='localhost', port=5000)