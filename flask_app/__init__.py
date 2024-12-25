from flask import Flask
from flask_sqlalchemy import SQLAlchemy # So we can use SQLAlchemy (via the flask-sqlalchemy package)
from flask_app.config import config # Has config settings for this app
from flask_migrate import Migrate # To allow database migrations - or create/update columns/tables (via the flask-migrate package)
from flask_wtf.csrf import CSRFProtect # To make all forms have CSRF tokens (via Flask-WTF package)

# App-level stuff is defined here, such as the app itself, secret and API keys (loaded from .env files), etc.
app = Flask(__name__)
app.config.from_object(config.Config) # Bring in class object directly, which has the needed config properties
csrf = CSRFProtect(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import models and routes here
from flask_app.models import user
from flask_app.controllers import user_controller, movie_controller # Bring in routes (at the end to avoid circular imports)