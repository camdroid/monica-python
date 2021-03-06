import pymysql.cursors
from config import db_host, db_user, db_pass, db_name


class DB(object):
    def __init__(self):
        self.db = pymysql.connect(
            host=db_host,
            user=db_user,
            password=db_pass,
            database=db_name,
            unix_socket='/tmp/mysql.sock',
            cursorclass=pymysql.cursors.DictCursor)
        # XXX Should make this idempotent, but just comment it out for now
        # self.create_database(db_name)

    def create_database(self, name):
        try:
            with self.db.cursor() as cursor:
                sql = "CREATE DATABASE IF NOT EXISTS %s" % name
                cursor.execute(sql)
            self.db.commit()
        finally:
            # self.db.close()
            pass

    def execute(self, query, params=None):
        with self.db.cursor() as cursor:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            res = []
            for row in cursor:
                res.append(row)
        return res

def get_db_conn():
    return DB()
