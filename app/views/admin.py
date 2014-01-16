from app import app
from flask import request, render_template, redirect, url_for
import libs.db_queries as db_proxy

@app.route('/admin/')
def admin_index():
	return "Hello Pluto."
	