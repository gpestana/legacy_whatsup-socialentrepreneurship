from app import db
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, Integer, String, ForeignKey


class EntriesTagsAssociation(db.Model):
	__tablename__ = "entries_tags_association"
	#id = Column(Integer, primary_key = True)
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

	picture = Column(String, nullable = False)
	main_url = Column(String, nullable=False)
	short_description = Column(String, nullable = False)
	loves = Column(Integer, nullable = False)
	content = Column(String, nullable = False)
	needed = Column(String, nullable = False)
	times_read = Column(Integer, nullable = False)


	def __init__(self, name, picture, main_url, short_description, content,\
		needed):
		self.name = name
		self.picture = picture
		self.main_url = main_url
		self.short_description = short_description
		self.content = content
		self.needed = needed
		self.loves = 0
		self.times_read = 0

	def __repr__(self):
		return 'Entry ID ' + str(self.id)

	def getID(self):
		return self.id

	def getTimesRead(self):
		return self.times_read
	def increaseTimesRead(self):
		self.times_read =+ 1


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
