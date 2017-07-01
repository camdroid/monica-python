import sys
sys.path.append('../monica-python')
sys.path.append('../monica-python/db')

import db
import unittest

class ContactsTest(unittest.TestCase):
    def setUp(self):
        self.db = db.database.get_db_conn()

    def test_get_contact(self):
        contacts = db.contacts.get_contacts(self.db)
        self.assertEqual(contacts[0]['cid'], 1)
        self.assertEqual(contacts[0]['name'], 'cam')

if __name__ == '__main__':
    unittest.main()
