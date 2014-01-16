import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.admin import Admin

app = Flask(__name__)

def init_db(db_name):
	app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL",\
		"postgresql+psycopg2://user:pass@localhost/"+db_name)
	return SQLAlchemy(app)


db = init_db("local_db")

from app import models
from views import general, admin, populate

db.create_all()