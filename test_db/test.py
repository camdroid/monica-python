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
        print(real.cid)
        actuals = db.contacts.get_contact(self.db, cid=real.cid)
        import pdb; pdb.set_trace()
        self.assertEqual(real, actuals[0])

if __name__ == '__main__':
    unittest.main()
