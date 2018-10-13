from flask import Flask, redirect, render_template, request, session, url_for
import base64
import database
import random
import os
import uuid
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './static/user_images/'
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg'])


app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


db = database.Database()


@app.route('/', methods = ['GET'])
def start():
    if 'user' not in session:
        image_list = db.get_random_images(10)
        return render_template('start.html', images=image_list)
    else:
        image_dict = db.get_random_images_and_title(20)
        # TODO: Get most liked images
        return render_template('homepage.html', user=session['user'], images=image_dict)


@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'GET':
        if 'user' in session:
            return redirect(url_for('start'))
        error = request.args.get('error', False)
        image = db.get_random_images(1)[0]
        return render_template('register.html', image=image, error=error)

    if request.method == 'POST':
        username = (request.form['username']).lower().strip()
        password = (request.form['password'])

        if db.check_username(username) == True:
            return redirect(url_for('register', error=True))
        else:
            db.add_user(username, password)
            session['user'] = username
            return redirect(url_for('start'))


@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        if 'user' in session:
            return redirect(url_for('start'))
        error = request.args.get('error', False)
        image = db.get_random_images(1)[0]
        return render_template('login.html', image=image, error=error)

    if request.method == 'POST':
        username = (request.form['username']).lower().strip()
        password = (request.form['password'])

        if db.check_username(username) == True:
            if db.check_password(username, password) == True:
                session['user'] = username
                return redirect(url_for('start'))
        return redirect(url_for('login', error=True))


@app.route('/search', methods = ['GET'])
def search():
    if request.method == 'GET':
        if 'user' in session:
            query = request.args.get('query').lower()
            image_dict = db.search(query)
            return render_template('search.html', user=session['user'], search=query, images=image_dict)
        else:
            return redirect(url_for('login'))


@app.route('/profile/<username>', methods = ['GET'])
def profile(username):
    if request.method == 'GET':
        if 'user' in session:
            image_dict = db.get_user_images(username)
            return render_template('profile.html', images=image_dict)
        else:
            return redirect(url_for('login'))


@app.route('/submit', methods = ['GET', 'POST'])
def submit():
    if request.method == 'GET':
        if 'user' not in session:
            return redirect(url_for('login'))
        else:
            return render_template('submit.html', user=session['user'])

    if request.method == 'POST':
        if 'user' not in session:
            return redirect(url_for('login'))
        else:
            image_id = str(base64.urlsafe_b64encode(str.encode(str(uuid.uuid4().fields[5]))))[2:-1][:6]
            file = request.files['imagefile']
            title = request.form['title']
            tags = [i.strip().lower() for i in request.form['tags'].split(',')]
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], image_id + ".jpg"))
            db.add_image(image_id, session['user'], title, tags)
            return redirect(url_for('profile', username=session['user']))


@app.route('/logout', methods = ['GET'])
def logout():
    if request.method == 'GET':
        if 'user' in session:
            del session['user']
        return redirect(url_for('start'))


if __name__ == '__main__':
    app.run(port=8080, debug=True)
