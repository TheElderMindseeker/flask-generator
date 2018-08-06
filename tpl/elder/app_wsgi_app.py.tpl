from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import application.config

app = Flask("FlaskApp")
app.config.from_object('application.config.Config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)
