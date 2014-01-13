from app import db
import app.models

def getEntries():
	return db.session.query(app.models.Entry).all()