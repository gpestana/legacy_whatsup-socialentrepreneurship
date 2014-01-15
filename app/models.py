from app import db
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, Integer, String, ForeignKey


class EntriesTagsAssociation(db.Model):
	__tablename__ = "entries_tags_association"
	entry_id = Column(Integer, ForeignKey('entries.id', ondelete="CASCADE"), primary_key = True)
	tag_id = Column(Integer, ForeignKey('tags.id', ondelete="CASCADE"), primary_key = True)
	
	def __init__(self):
		pass
	def __repr__(self):
		return 'Associaltion Entry+Tag: ' +str(self.entry_id)+", "+str(self.tag_id)


class Entry(db.Model):
	__tablename__ = "entries"
	id = Column(Integer, primary_key = True)
	name = Column(String, nullable = False)
	tags = relationship(EntriesTagsAssociation, backref="entries")

	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return 'Entry ID ' + str(self.id)

	def getID(self):
		return self.id

class Tag(db.Model):
	__tablename__ = "tags"
	id = Column(Integer, primary_key = True)
	name = Column(String, nullable = False)

	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return 'Tag ID '+ str(self.id)

	def getID(self):
		return self.id
