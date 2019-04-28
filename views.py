from myapp import app
from models import Member
from forms import LoginForm
from flask import render_template

@app.route('/')
def index():
    firstmember = Member.query.first()
    return '<h1>The first member is: '+ firstmember.name +'</h1>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('index.html', form=form)

@app.route('/user/<username>')
def show_user_profile(username):
    # Show user profile for the user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # Show the post with the given id, the id is an integer
    return 'Post %d' %post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/ (e.g 127.0.0.1:5000/path/hello/world)
    return 'Subpath %s' % subpath

@app.route('/float/<float:decimal>')
def show_float(decimal):
    # show a decimal number
    return 'Decimal %.5f' % decimal

