from flask import Flask
from flask_sqlalchemy_core import FlaskSQLAlchemy
import os

app = Flask(__name__)


# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
app.config["DEBUG"] = True

# Secret key for session management. You can generate random strings here:
# https://randomkeygen.com/
app.config["SECRET_KEY"] = '731958285'

# Connect to the database
#app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://dbproj:DBMS2020@localhost/socialdb'

db = FlaskSQLAlchemy('mysql+pymysql://dbproj:DBMS2020@localhost/socialdb')
from app import views
