import pymysql.cursors
class MySQLConnection:
    def __init__(self, db, db_host, db_user, db_pass):
        connection = pymysql.connect(host = db_host, user = db_user, password = db_pass, db = db, charset = 'utf8mb4', cursorclass = pymysql.cursors.DictCursor, autocommit = True)
        self.connection = connection
    def query_db(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print('\nRunning Query:', query, '\n')

                executable = cursor.execute(query, data)
                if query.lower().find("insert") >= 0:
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().find("select") >= 0:
                    result = cursor.fetchall()
                    return result
                else:
                    self.connection.commit()
            except Exception as e:
                print("Something went wrong", e)
                return False
def connectToMySQL(db, db_host, db_user, db_pass):
    return MySQLConnection(db, db_host, db_user, db_pass)
