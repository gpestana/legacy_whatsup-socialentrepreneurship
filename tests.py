import os
import unittest
import app.views.libs.db_queries as db_proxy
from app import app, db, init_db


class TestSequenceBasic(unittest.TestCase):

	def setUp(self):
		default_setup()
		
	def tearDown(self):
		db_proxy.deleteAll()
	

	#REST 
	def testGetEntriesChronologically(self):
		entries = db_proxy.getEntriesChronologically()
		self.assertGreater(entries[0].getID(), entries[1].getID())

	def testGetEntriesReverseChronologically(self):
		entries = db_proxy.getEntriesReverseChronologically()
		self.assertGreater(entries[1].getID(), entries[0].getID())

	def testGetEntriesByTimesRead(self):
		entry1 = db_proxy.getEntryByName("def_entry1")
		entry2 = db_proxy.getEntryByName("def_entry2")
		entry3 = db_proxy.getEntryByName("def_entry3")

		db_proxy.increaseTimesRead(entry1.getID())
		db_proxy.increaseTimesRead(entry2.getID())
		db_proxy.increaseTimesRead(entry2.getID())

		entries = db_proxy.getEntriesByTimesRead()

		self.assertEqual(entries[0].getID(), entry2.getID())
		self.assertEqual(entries[1].getID(), entry1.getID())
		self.assertEqual(entries[2].getID(), entry3.getID())


	def testGetNumberEntries(self):
		nr = 2
		entries = db_proxy.getEntriesChronologically(nr)
		self.assertEqual(len(entries), 2)

	def testGetEntriesPopularity(self):
		print "test2"

	def testGetEntriesByTag(self):
		tag = db_proxy.getTagByName("def_tag1")
		entry = db_proxy.getEntryByName("def_entry1")

		entries = db_proxy.getAllEntriesTag(tag.getID())

		self.assertEqual(len(entries), 1)
		self.assertEqual(entries[0].entry_id, entry.getID())

	def testTimesEntryRead(self):
		entry = db_proxy.getEntryByName("def_entry1")
		self.assertEqual(entry.getTimesRead(), 0)

		db_proxy.increaseTimesRead(entry.getID())
		self.assertEqual(entry.getTimesRead(), 1)


	#ADMIN
	def testAddTagToEntry(self):
		tag1 = db_proxy.getTagByName("def_tag1")
		tag2 = db_proxy.getTagByName("def_tag2")
		entry = db_proxy.getEntryByName("def_entry1")

		db_proxy.addTagToEntry(entry.getID(), tag2.getID())		

		entries = db_proxy.getAllEntriesTag(tag1.getID())
		tags = db_proxy.getAllTagsEntry(entry.getID())

		self.assertEqual(entries[0].entry_id, entry.getID())
		self.assertEqual(len(tags), 2)
	

	def testRemoveTagFromEntry(self):
		tag = db_proxy.getTagByName("def_tag1")
		entry = db_proxy.getEntryByName("def_entry1")

		db_proxy.removeTagFromEntry(entry.getID(), tag.getID())

		self.assertEqual(db_proxy.getAllTagsEntry(entry.getID()), [])

	def testRemoveTagSimple(self):
		tag = db_proxy.addTag("tag3")
		db_proxy.removeTag(tag.getID())
		self.assertEqual(db_proxy.getTagByName("tag3"), None)


	def testRemoveTagAssignedToEntry(self):
		tag = db_proxy.getTagByName("def_tag1")
		entry = db_proxy.getEntryByName("def_entry1")
		db_proxy.removeTagFromEntry(entry.getID(), tag.getID())
	
		association = db_proxy.getAllEntriesTag(tag.getID())

		self.assertEqual(len(association), 0)

		db_proxy.removeTag(tag.getID())
		self.assertEqual(db_proxy.getTagByName("tag1"), None)


	def testRemoveEntry(self):
		entry = db_proxy.getEntryByName("def_entry1")

		db_proxy.removeEntry(entry.getID())

		self.assertEqual(db_proxy.getEntryByName("def_entry1"), None)
		self.assertEqual(len(db_proxy.\
			getAllEntriesTag(db_proxy.getTagByName("def_tag1").getID())), 0)


class TestSequenceSearch(unittest.TestCase):

	def setUp(self):
		default_setup()
		print "init"

	def tearDown(self):
		db_proxy.deleteAll()

	def testSearchEntry(self):
		print "test6"
	

def default_setup():
	def_entry1 = db_proxy.addEntry("def_entry1", "picture", "main_url",\
		"short_description", "content", "needed")
	def_entry2 = db_proxy.addEntry("def_entry2", "picture", "main_url",\
		"short_description", "content", "needed")
	def_entry3 = db_proxy.addEntry("def_entry3", "picture","main_url",\
		"short_description", "content", "needed")

	def_tag1 = db_proxy.addTag("def_tag1")
	def_tag2 = db_proxy.addTag("def_tag2")

	db_proxy.addTagToEntry(def_entry1.getID(), def_tag1.getID())

def init_testing_db():
	app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', \
	'postgresql+psycopg2://user:pass@localhost/test')
	db.create_all()

if __name__ == "__main__":
	init_testing_db()
	db_proxy.deleteAll()
	unittest.main()
