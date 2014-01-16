from app import app
from flask import request, render_template, redirect, url_for
import libs.db_queries as db_proxy
from app.forms import TestForm

@app.route('/')
def index():
	entries = db_proxy.getEntriesChronologically(10)
	return render_template("index.html", entries = entries)

@app.route('/startup/<name>')
def startup(name):
	return "Hello Mars. - Startup"


@app.route('/manifesto/')
def manifesto():
	return "Hello Mars. - Manifesto"


@app.route('/contribute/')
def contribute():
	return "Hello Mars. - Contribute"
