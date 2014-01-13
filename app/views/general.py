from app import app
from flask import request, render_template, redirect, url_for
import libs.db_queries as db_proxy
from app.forms import TestForm

@app.route('/')
def index():
	
	for entry in db_proxy.getEntries():
		print entry

	form = TestForm(request.form)

	return "Hello Mars."
	