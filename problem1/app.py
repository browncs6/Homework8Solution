from flask import Flask, render_template, request
from glob import glob
from random import choice

app = Flask(__name__, static_url_path='', static_folder='static', template_folder='templates')


# route for http://127.0.0.1:5000/
@app.route('/')
def home():
    return render_template('home.html')


# route for http://127.0.0.1:5000/hello
@app.route('/hello')
def hello_world():
    return '<!DOCTYPE html><html><b>hello world!</b></html>'


# route for http://127.0.0.1:5000/about
@app.route('/about')
def about():
    return render_template('about.html')


# route for http://127.0.0.1:5000/greet
# route for http://127.0.0.1:5000/greet?user=<>&msg=<>
@app.route('/greet', methods=['POST', 'GET'])
def greet():
    user = ""
    msg = ""
    if request.method == 'POST':
        user = request.values.get('user')
        msg = request.values.get('msg')
    elif request.method == 'GET':
        user = request.args.get('user')
        msg = request.args.get('msg')
    pics = glob('static/img/*.png')
    pics = [pic.split("/")[-1] for pic in pics]
    if user.lower() == 'tux':
        pic = 'tux.png'
    else:
        pics.remove('tux.png')
        pic = choice(pics)
    return render_template('home.html', user=user, msg=msg, pic=pic)


if __name__ == '__main__':
    app.run(debug=True)
