import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)


#local DB
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL",\
	"postgresql+psycopg2://user:pass@localhost/local_db")

db = SQLAlchemy(app)

from app import models
from views import general

db.create_all()