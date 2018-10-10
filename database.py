import pymysql
from werkzeug.security import generate_password_hash, check_password_hash

class Database:
    def __init__(self):
        password = open('password.txt').read().strip()
        self.db = pymysql.connect(host='localhost', user='root', passwd=password, db='unsplash')
        self.cur = self.db.cursor()

    def add_user(self, username, plain_password):
        hash = generate_password_hash(plain_password)
        try:
            self.cur.execute(f'INSERT INTO users VALUES("{username}", "{hash}")')
            self.db.commit()
        except:
            self.db.rollback()

    def check_username(self, username):
        self.cur.execute(f'SELECT COUNT(*) FROM users WHERE username = "{username}"')
        if self.cur.fetchone()[0] == 0:
            return False
        return True

    def check_password(self, username, plain_password):
        self.cur.execute(f'SELECT password FROM users WHERE username = "{username}"')
        hash = self.cur.fetchone()[0]
        return check_password_hash(hash, plain_password)
