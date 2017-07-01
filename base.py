from db.database import DB

class Base(object):
    def __init__(self):
        self.db = DB()
