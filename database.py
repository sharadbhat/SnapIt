import pymysql
import json
from werkzeug.security import generate_password_hash, check_password_hash

class Database:
    def __init__(self):
        config = json.load(open('db_config.json'))
        self.db = pymysql.connect(host=config['host'], user=config['user'], passwd=config['passwd'], db=config['db'])
        self.cur = self.db.cursor()

    def get_random_images(self, n):
        self.cur.execute(f'SELECT id FROM images ORDER BY RAND() LIMIT {n}')
        images = []
        for i in self.cur.fetchall():
            images.append(i[0])
        return images

    def get_random_images_and_data(self, n):
        self.cur.execute(f'SELECT id, title, uploader, likes FROM images ORDER BY RAND() LIMIT {n}')
        images = {}
        for i in self.cur.fetchall():
            images[i[0]] = i[1:]
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

    def delete_image(self, image_id):
        try:
            self.cur.execute(f'DELETE FROM favourites WHERE id = "{image_id}"')
            self.cur.execute(f'DELETE FROM images WHERE id = "{image_id}"')
            self.db.commit()
        except:
            self.db.rollback()

    def get_details(self, image_id):
        self.cur.execute(f'SELECT id, title, uploader, likes FROM images WHERE id = "{image_id}"')
        return self.cur.fetchone()

    def is_liked(self, username, image_id):
        self.cur.execute(f'SELECT COUNT(*) FROM favourites WHERE username = "{username}" AND id = "{image_id}"')
        return 1 == self.cur.fetchone()[0]

    def add_to_fav(self, username, image_id):
        try:
            self.cur.execute(f'INSERT INTO favourites VALUES("{username}", "{image_id}")')
            self.cur.execute(f'UPDATE images SET likes = likes + 1 WHERE id = "{image_id}"')
            self.db.commit()
        except:
            self.db.rollback()

    def remove_from_fav(self, username, image_id):
        try:
            self.cur.execute(f'DELETE FROM favourites WHERE username = "{username}" AND id = "{image_id}"')
            self.cur.execute(f'UPDATE images SET likes = likes - 1 WHERE id = "{image_id}"')
            self.db.commit()
        except:
            self.db.rollback()

    def get_fav(self, username):
        self.cur.execute(f'SELECT images.id, images.title, images.uploader, images.likes FROM images, favourites WHERE images.id = favourites.id AND favourites.username = "{username}"')
        details = {}
        for i in self.cur.fetchall():
            details[i[0]] = i[1:]
        return details

    def search(self, query):
        self.cur.execute(f'SELECT id, title, uploader, likes FROM images WHERE tags LIKE "%{query}%"')
        images = {}
        for i in self.cur.fetchall():
            images[i[0]] = i[1:]
        return images

    def get_user_images(self, username):
        self.cur.execute(f'SELECT id, title, likes FROM images WHERE uploader = "{username}"')
        images = {}
        for i in self.cur.fetchall():
            images[i[0]] = i[1:]
        return images
