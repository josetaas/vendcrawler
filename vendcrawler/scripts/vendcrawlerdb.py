import pymysql.cursors

import vendcrawler

class VendCrawlerDB(object):

    def __init__(self, user, password, database):
        self.host = 'localhost'
        self.user = user
        self.password = password
        self.database = database

    def insert(self, table, columns, values):
        connection = self.connect()
        try:
            for value in values:
                query = "INSERT INTO " + table + " ("
                for column in columns:
                    query += column + ','

                # remove last comma
                query = query[:-1]
                query += ") VALUES ("
                for i in range(0, len(value)):
                    query += '%s,'

                query = query[:-1]
                query += ")"

                with connection.cursor() as cursor:
                    cursor.execute(query, tuple(value))

            connection.commit()
        finally:
            connection.close()

    def connect(self):
        return pymysql.connect(host=self.host,
                               user=self.user,
                               password=self.password,
                               db=self.database,
                               cursorclass=pymysql.cursors.DictCursor)
