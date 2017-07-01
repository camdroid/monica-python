import pymysql.cursors


class DB(object):
    def __init__(self):
        self.connection = pymysql.connect(
            host='127.0.0.1',
            user='root',
            password='',
            cursorclass=pymysql.cursors.DictCursor)
        self.create_database()

    def create_database(self):
        try:
            with connection.cursor() as cursor:
                sql = 'CREATE DATABASE IF NOT EXISTS `monica-python`'
                cursor.execute(sql)
            connection.commit()
        finally:
            connection.close()
