import pymysql
from werkzeug.security import generate_password_hash, check_password_hash

class Database:
    def __init__(self):
        password = open('password.txt').read().strip()
        self.db = pymysql.connect(host='localhost', user='root', passwd=password, db='unsplash')
        self.cur = self.db.cursor()

    def get_random_images(self, n):
        self.cur.execute(f'SELECT id FROM images ORDER BY RAND() LIMIT {n}')
        images = []
        for i in self.cur.fetchall():
            images.append(i[0])
        return images

    def get_random_images_and_title(self, n):
        self.cur.execute(f'SELECT id, title FROM images ORDER BY RAND() LIMIT {n}')
        images = {}
        for i in self.cur.fetchall():
            images[i[0]] = i[1]
        return images

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

    def add_image(self, image_id, username, title, tags):
        try:
            tags = " ".join(tags)
            self.cur.execute(f'INSERT INTO images VALUES("{image_id}", "{title}", "{username}", 0, "{tags}")')
            self.db.commit()
        except:
            self.db.rollback()

    def search(self, query):
        self.cur.execute(f'SELECT id, title FROM images WHERE tags LIKE "%{query}%"')
        images = {}
        for i in self.cur.fetchall():
            images[i[0]] = i[1]
        return images

    def get_user_images(self, username):
        self.cur.execute(f'SELECT id, title FROM images WHERE uploader = "{username}"')
        images = {}
        for i in self.cur.fetchall():
            images[i[0]] = i[1]
        return images
