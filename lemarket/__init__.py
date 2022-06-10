from flask import Flask
from flask_sqlalchemy import SQLAlchemy
webapp = Flask(__name__) 
webapp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///monacemebi.db'
webapp.config['SECRET_KEY'] = 'paroli'
db = SQLAlchemy(webapp)
from lemarket import routes
