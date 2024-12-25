import os, secrets
from dotenv import load_dotenv # Bring in .env values (via python-dotenv package)
load_dotenv()

class Config:
    # Secret key, loaded from .env file - or generate one cryptographically
    SECRET_KEY = os.getenv("SECRET_KEY") or secrets.token_hex() # Future: raise error if secret key is NOT loaded
    # Database URI (for Flask-SQLAlchemy) - more info on linking here: https://docs.sqlalchemy.org/en/20/dialects/mysql.html#module-sqlalchemy.dialects.mysql.pymysql
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://" + os.getenv("SQL_USERNAME") + ":" + os.getenv("SQL_PASSWORD") + \
        "@localhost:" + os.getenv("SQL_PORT_NUMBER")+"/"+os.getenv("SQL_DB_NAME") # String format: dialect://username:password@host:port/database
