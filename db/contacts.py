from base import Base


class Contact(Base):
    def __init__(self, cid=None, name=''):
        self.cid = cid
        self.name = name

def add_contact(db, contact):
    db.execute('INSERT INTO contacts (name) VALUES (%s)', (contact.name,))
    res = db.execute('SELECT * FROM contacts WHERE name=%s', (contact.name,))
    contact = Contact(res[0]['cid'], res[0]['name'])
    return contact

def get_contacts(db):
    contacts = db.execute('SELECT * FROM contacts')
    return contacts

def get_contact(db, cid):
    return db.execute('SELECT * FROM contacts WHERE cid=%s', (cid,))

