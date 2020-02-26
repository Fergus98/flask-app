 # import Flask class from the flask module
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
from os import getenv


 # create a new instance of Flask and store it in app 
app = Flask(__name__)

bcrypt = Bcrypt(app)
app.config['SECRET_KEY'] = str(os.getenv('MY_SECRET_KEY'))

login_manager = LoginManager(app)
login_manager.login_view = 'login'

app.config["SQLALCHEMY_DATABASE_URI"] = str(os.getenv('DATABASE_URI'))
db = SQLAlchemy(app)
 # import the ./application/routes.py fi
from application import routes
