import os
import unittest
import app.views.libs.db_queries as db_proxy
from app import app, db, init_db


class TestSequenceEntries(unittest.TestCase):

	def setUp(self):
		db_proxy.addEntry("entry1")
		db_proxy.addEntry("entry2")
		db_proxy.addEntry("entry3")

	def tearDown(self):
		db_proxy.deleteAll()
	

	#REST 
	def testGetEntriesChronologically(self):
		entries = db_proxy.getEntriesChronologically()
		self.assertGreater(entries[0].getID(), entries[1].getID())

	def testGetNumberEntries(self):
		nr = 2
		entries = db_proxy.getEntriesChronologically(nr)
		self.assertEqual(len(entries), 2)

	def testGetEntriesPopularity(self):
		print "test2"

	def testGetEntriesByTag(self):
		tag2 = db_proxy.addTag("tag2")
		entry = db_proxy.addEntry("entry")
		db_proxy.addTagToEntry(entry.getID(), tag2.getID())

		entries = db_proxy.getAllEntriesTag(tag2.getID())

		self.assertEqual(len(entries), 1)
		self.assertEqual(entries[0].entry_id, entry.getID())


	def testAddTagToEntry(self):
		tag1 = db_proxy.addTag("tag1")
		tag2 = db_proxy.addTag("tag2")
		entry = db_proxy.addEntry("entry")

		db_proxy.addTagToEntry(entry.getID(), tag1.getID())
		db_proxy.addTagToEntry(entry.getID(), tag2.getID())

		entries = db_proxy.getAllEntriesTag(tag1.getID())
		tags = db_proxy.getAllTagsEntry(entry.getID())

		self.assertEqual(entries[0].entry_id, entry.getID())
		self.assertEqual(len(tags), 2)

	def testRemoveTagFromEntry(self):
		tag1 = db_proxy.addTag("tag1")
		entry = db_proxy.addEntry("entry")
		db_proxy.addTagToEntry(entry.getID(), tag1.getID())

		db_proxy.removeTagFromEntry(entry.getID(), tag1.getID())

		self.assertEqual(db_proxy.getAllTagsEntry(entry.getID()), [])


class TestSequenceSearch(unittest.TestCase):

	def setUp(self):
		#init_db("test")
		print "init"

	def tearDown(self):
		db_proxy.deleteAll()

	def testSearchEntry(self):
		print "test6"


class TestSequenceTags(unittest.TestCase):


	def setUp(self):
		print "init"

	def tearDown(self):
		db_proxy.deleteAll()

	def testAddTag(self):
		print "test"

	def testRemoveTag(self):
		print "test"

	def testEditTag(self):
		print "test"

	def testEditEntry(self):
		print "test5"


def init_testing_db():
	app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', \
	'postgresql+psycopg2://user:pass@localhost/test')
	db.create_all()

if __name__ == "__main__":
	init_testing_db()
	unittest.main()
