import pymysql.cursors
from config import db_host, db_user, db_pass, db_name


class DB(object):
    def __init__(self):
        self.db = pymysql.connect(
            host=db_host,
            user=db_user,
            password=db_pass,
            cursorclass=pymysql.cursors.DictCursor)
        self.create_database(db_name)

    def create_database(self, name):
        try:
            with self.db.cursor() as cursor:
                sql = "CREATE DATABASE IF NOT EXISTS %s" % name
                cursor.execute(sql)
            self.db.commit()
        finally:
            self.db.close()

    def get_db_conn(self):
        return self.db
