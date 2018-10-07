from flask import Flask, redirect, render_template, request, session, url_for
import random
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

def get_random_images(n):
    files = os.listdir('static/images/backgrounds')
    return random.sample(files, n)

@app.route('/', methods = ['GET'])
def start():
    image_list = get_random_images(3)
    return render_template('start.html', images = image_list)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        if 'user' in session:
            return redirect(url_for('start'))
        image = get_random_images(1)[0]
        return render_template('login.html', image = image)

    if request.method == 'POST':
        username = (request.form['username']).lower().strip()
        password = (request.form['password'])
        return redirect(url_for('start'))

@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'GET':
        if 'user' in session:
            return redirect(url_for('start'))
        image = get_random_images(1)[0]
        return render_template('register.html', image = image)

    if request.method == 'POST':
        username = (request.form['username']).lower().strip()
        password = (request.form['password'])
        return redirect(url_for('start'))

if __name__ == '__main__':
    app.run(port=8080, debug=True)
