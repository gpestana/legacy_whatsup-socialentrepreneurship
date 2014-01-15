from app import app
from flask import request, render_template, redirect, url_for
import libs.db_queries as db_proxy
from app.forms import TestForm

@app.route('/')
def index():
	
	#db_proxy.addEntry("entry1")
	#db_proxy.addTag("tag1")
	#db_proxy.addEntry("entry2")
	#db_proxy.addTag("tag2")

	db_proxy.addTagToEntry(10,5)
	db_proxy.removeTagFromEntry(10,5)

	for entry in db_proxy.getEntriesChronologically():
		print entry

	#form = TestForm(request.form)

	return "Hello Mars."
	