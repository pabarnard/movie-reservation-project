from flask import Flask
from dotenv import load_dotenv # Bring in .env values (via python-dotenv package)
import os # Used in conjuction with the python-dotenv package
# App-level stuff is defined here, such as the app itself, secret and API keys (loaded from .env files), etc.
app = Flask(__name__)
load_dotenv() # Bring in variables from .env file
app.secret_key = os.getenv("SECRET_KEY") # Secret key, loaded from .env file

from flask_app.controllers import movie_controller # Bring in routes (at the end to avoid circular imports)