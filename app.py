from flask import Flask, redirect, render_template, request, session, url_for
import database
import random
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

db = database.Database()

def get_random_images(page, n):
    subfolder = 'start'
    if page == 1:
        subfolder = 'login'
    files = os.listdir(f'static/images/backgrounds/{subfolder}')
    return random.sample(files, n)

@app.route('/', methods = ['GET'])
def start():
    if 'user' in session:
        image_list = get_random_images(0, 10)
        return render_template('start.html', images = image_list)
    else:
        image_list = get_random_images(1, 10)
        return render_template('homepage.html', images = image_list)

@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'GET':
        if 'user' in session:
            return redirect(url_for('start'))
        image = get_random_images(1, 1)[0]
        return render_template('register.html', image = image, error = False)

    if request.method == 'POST':
        username = (request.form['username']).lower().strip()
        password = (request.form['password'])
        # TODO: Check credentials and go to correct page
        return redirect(url_for('start'))

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        if 'user' in session:
            return redirect(url_for('start'))
        image = get_random_images(1, 1)[0]
        return render_template('login.html', image = image, error = False)

    if request.method == 'POST':
        username = (request.form['username']).lower().strip()
        password = (request.form['password'])
        # TODO: Check credentials and go to correct page
        return redirect(url_for('start'))

@app.route('/logout', methods = ['GET'])
def logout():
    if request.method == 'GET':
        if 'user' in session:
            del session['user']
        return redirect(url_for('start'))

if __name__ == '__main__':
    app.run(port=8080, debug=True)
