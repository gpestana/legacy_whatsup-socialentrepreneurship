from app import app
from flask import request, render_template, redirect, url_for
import libs.db_queries as db_proxy

@app.route('/populate/')
def populate():

	def_entry1 = db_proxy.addEntry("def_entry1", "picture", "main_url",\
		"short_description", "content", "needed")
	def_entry2 = db_proxy.addEntry("def_entry2", "picture", "main_url",\
		"short_description", "content", "needed")
	def_entry3 = db_proxy.addEntry("def_entry3", "picture","main_url",\
		"short_description", "content", "needed")

	def_tag1 = db_proxy.addTag("def_tag1")
	def_tag2 = db_proxy.addTag("def_tag2")

	db_proxy.addTagToEntry(def_entry1.getID(), def_tag1.getID())

	return "DB populated successfully!"

@app.route('/clean/')
def clean():
	db_proxy.deleteAll()

	return "DB cleaned successfully!"	