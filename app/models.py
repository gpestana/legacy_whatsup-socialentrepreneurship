from app import db
from sqlalchemy import Column, Integer, String

class Entry(db.Model):
	__tablename__ = "entries"
	id = Column(Integer, primary_key = True)
	name = Column(String, nullable = False)

	def __init__(self):
		self.name = "Entry Name"

	def __repr__(self):
		return 'Entry ID' + str(self.id)
