from base import Base


class Contact(Base):
    def __init__(self, cid=None, name=''):
        self.cid = cid
        self.name = name

    @classmethod
    def map(cls, c_dict):
        return cls(cid=c_dict['cid'], name=c_dict['name'])

    def __eq__(self, other):
        if self.cid != other.cid:
            return False
        if self.name != other.name:
            return False
        return True

def add_contact(db, contact):
    db.execute('INSERT INTO contacts (name) VALUES (%s)', (contact.name,))
    res = db.execute('SELECT * FROM contacts WHERE name=%s', (contact.name,))
    contact = Contact.map(res[0])
    return contact

def get_contacts(db):
    contacts = db.execute('SELECT * FROM contacts')
    contacts = [Contact.map(res) for res in contacts]
    return contacts

def get_contact(db, cid):
    res = db.execute('SELECT * FROM contacts WHERE cid=%s', (cid,))
    return Contact.map(res[0])

