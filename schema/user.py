import mysql.connector
from mysql.connector import Error


class UserDb:
    __tablename__ = "tbl_user"
    host = 'localhost'
    user = 'study'
    password = 'tmxjel0001!'
    db = 'studydb'
    connector_ = None

    # port = 3306
    def __init__(self):
        if UserDb.connector_ is None:
            UserDb.connector = \
                mysql.connector.connect(host=UserDb.host,
                                        user=UserDb.user,
                                        password=UserDb.password,
                                        database=UserDb.db,
                                        charset='utf8')
        self.cursor = UserDb.connector.cursor()

    def create_user(self, email, password):
        self.cursor.callproc('pr_create_tbl_user', [email, password])
        for result in self.cursor.stored_results():
            return result.fetchall()[0][0]


def close(self):
    self.cursor.close()
    print("User db is closed.")
