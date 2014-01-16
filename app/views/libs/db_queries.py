from app import db
import app.models


#ENTRIES
def getEntryByID(id):
	return db.session.query(app.models.Entry).\
	filter(app.models.Entry.id == id).first()

def getEntryByName(name):
	return db.session.query(app.models.Entry).\
	filter(app.models.Entry.name == name).first()

def addEntry(name, picture, main_url, short_description, content,\
		needed):
	entry = app.models.Entry(name, picture, main_url, short_description,\
	 content, needed)
	db.session.add(entry)
	db.session.commit()
	return entry

def removeEntry(entry_id):
	entry = db.session.query(app.models.Entry).\
	filter(app.models.Entry.id == entry_id).first()
	associations = db.session.query(app.models.EntriesTagsAssociation).\
	filter(app.models.EntriesTagsAssociation.entry_id == entry_id).all()

	for association in associations:
		db.session.delete(association)
		db.session.commit()

	db.session.delete(entry)
	db.session.commit()


"""Returns all entries ordered from newest to oldest
"""
def getEntriesChronologically(nr_posts = None):
	return db.session.query(app.models.Entry).limit(nr_posts).all()[::-1]

"""Returns all entries ordered from newest to oldest
"""
def getEntriesReverseChronologically(nr_posts = None):
	return db.session.query(app.models.Entry).limit(nr_posts).all()

"""Returns all entries ordered from most visited to the least
"""
def getEntriesByTimesRead(nr_posts = None):
	return db.session.query(app.models.Entry).\
	order_by(app.models.Entry.times_read).limit(nr_posts).all()[::-1]

def increaseTimesRead(entry_id):
	entry = getEntryByID(entry_id)
	entry.increaseTimesRead()


#Association TAGS-ENTRIES
def addTagToEntry(entry_id, tag_id):
	entry = getEntryByID(entry_id)
	association = app.models.EntriesTagsAssociation()

	association.tag_id = tag_id
	association.entry_id = entry_id

	entry.tags.append(association)
	db.session.commit()

def getAllEntriesTag(tag_id):
	return db.session.query(app.models.EntriesTagsAssociation).\
	filter(app.models.Tag.id == tag_id).all()

def getAllTagsEntry(entry_id):
	return db.session.query(app.models.EntriesTagsAssociation).\
	filter(app.models.Entry.id == entry_id).all()

def removeTagFromEntry(entry_id, tag_id):
	association = db.session.query(app.models.EntriesTagsAssociation).\
	filter(app.models.Tag.id == tag_id).\
	filter(app.models.Entry.id == entry_id).first()

	db.session.delete(association)
	db.session.commit()


#TAGS
def addTag(name):
	tag = app.models.Tag(name)
	db.session.add(tag)
	db.session.commit()
	return tag

def getTagByID(tag_id):
	return db.session.query(app.models.Tag).\
	filter(app.models.Tag.id == tag_id).first()

def getTagByName(tag_name):
	return db.session.query(app.models.Tag).\
	filter(app.models.Tag.name == tag_name).first()

def removeTag(tag_id):
	tag = getTagByID(tag_id)
	db.session.delete(tag)
	db.session.commit()


#Helpers
def deleteAll():
	app.models.Entry.query.delete()
	db.session.commit()
	app.models.Tag.query.delete()
	db.session.commit()
	app.models.EntriesTagsAssociation.query.delete()
	db.session.commit()
