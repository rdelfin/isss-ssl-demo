from flask import render_template, send_from_directory, request
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    return render_template('index.html',
                           title='Home',
                           user=user)

@app.route('/form', methods=['POST'])
def form():
    print("PASSWORD ENTERED: {}".format(request.form["password"]))
    return render_template('form.html')
    

@app.route('/static/<path:path>')
def send_js(path):
    return send_from_directory('static', path)
