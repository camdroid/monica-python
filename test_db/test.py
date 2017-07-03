import sys
sys.path.append('../monica-python')
sys.path.append('../monica-python/db')

import db
import unittest

class ContactsTest(unittest.TestCase):
    def setUp(self):
        self.db = db.database.get_db_conn()

    def test_get_contact(self):
        # Without having add_contact working, can't test that it's reading.
        # Just check it's not failing.
        contacts = db.contacts.get_contacts(self.db)

    def test_add_contact(self):
        contact = db.contacts.Contact('cam')
        real = db.contacts.add_contact(self.db, contact)
        actual = db.contacts.get_contact(self.db, cid=real.cid)
        self.assertEqual(real, actual)

if __name__ == '__main__':
    unittest.main()
