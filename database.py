import pymysql
from werkzeug.security import generate_password_hash, check_password_hash

class Database:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', passwd='shamanmb', db='unsplash')
        self.cur = self.db.cursor()

    def add_user(self, username, plain_password):
        pass

    def check_username(self, username):
        pass

    def check_password(self, plain_password):
        pass
