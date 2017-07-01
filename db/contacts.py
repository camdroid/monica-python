from base import Base


class Contact(Base):
    def __init__(self):
        pass

def add_contact(db):
    pass

def get_contacts(db):
    contacts = db.execute('SELECT * FROM contacts')
    return contacts

