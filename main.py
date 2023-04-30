from flask import Flask, flash, redirect, url_for, render_template, session
from flask import request

from flask_sqlalchemy import SQLAlchemy

from db.db_connect import DB_HOST, DB_NAME, DB_USERNAME, DB_PASSWORD

import datetime

# DB_HOST = "localhost"
# DB_NAME = "sandwich_maker"
# DB_USERNAME = "root"
# DB_Password = "root"

database_file = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:3306/{DB_NAME}"

app = Flask(__name__)
app.secret_key = "mysecret"
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)


@app.before_request
def initialize_session():
    if 'username' not in session:
        session['username'] = None
    if 'user-uid' not in session:
        session['user-uid'] = None


class UserCredentials(db.Model):
    __tablename__ = 'user_credentials'
    uid = db.Column(db.Integer(), primary_key=True, nullable=False)
    username = db.Column(db.String(36), nullable=False)
    password = db.Column(db.String(20), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password


class UserPost(db.Model):
    __tablename__ = 'user_posts'
    uid = db.Column(db.Integer(), primary_key=True, nullable=False, autoincrement=True)
    user = db.Column(db.Integer(), nullable=False)
    timePosted = db.Column(db.DateTime(), nullable=False)
    text = db.Column(db.String(280), nullable=False)


@app.route("/")
def home_implicit():
    return redirect("/welcome")


# Logs the user in. Called after details are validated. Returns false if an error occurred.
def log_user_in(username, user_uid):
    session['username'] = username
    session['user-uid'] = user_uid
    return True


def log_user_out():
    session['username'] = None
    session['user-uid'] = None
    return True


def get_post_by_uid(post_uid):
    return UserPost.query.filter_by(uid=post_uid).first()


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if not request.form['username'] or not request.form['password']:
            flash('Missing required fields', 'error')
        else:
            username = request.form['username']
            user_entry = UserCredentials.query.filter_by(username=username).first()
            if not user_entry:
                flash("Invalid username", category="error")
                print("Bad username")
            elif user_entry.password == request.form['password']:
                succ = log_user_in(username, user_entry.uid)
                if succ:
                    flash('Login successful', 'success')
                    return redirect("/welcome")
                else:
                    flash('Unknown error while logging in', category="error")
            else:
                flash("Incorrect password", category="error")
    return render_template('login.html')


@app.route('/logout', methods=['GET'])
def logout():
    log_user_out()
    return redirect("/")


@app.route('/welcome', methods=['GET'])
def welcome():
    query = UserPost.query
    posts = query.all()

    # Adds data for the webpage that is not in the database entry
    for i in range(0, len(posts)):
        # Translates user UID to username
        name = UserCredentials.query.filter_by(uid=posts[i].user).first().username
        timePosted = posts[i].timePosted
        timePostedText = timePosted.strftime("%I:%M %p").lstrip('0') + " " + timePosted.strftime("%d %B, %Y")
        posts[i] = {"username": name, "timePostedText": timePostedText, "data": posts[i]}

    return render_template('welcome.html', username=session['username'], posts=posts)


@app.route('/editpost/<post_uid>', methods=['GET', 'POST'])
def edit_post(post_uid):
    post = get_post_by_uid(post_uid)
    if request.method == 'POST':
        post.text = request.form['text']
        db.session.commit()
        return redirect("/home")
    return render_template('edit-post.html', post=post)


@app.route('/removepost/<post_uid>', methods=['GET'])
def remove_post(post_uid):
    UserPost.query.filter_by(uid=post_uid).delete()
    db.session.commit()
    return redirect('/home')


@app.route('/users/<homepage_username>', methods=['GET'])
def homepage(homepage_username):
    user = UserCredentials.query.filter_by(username=homepage_username).first()

    posts = UserPost.query.all()
    # Adds data for the webpage that is not in the database entry
    for i in range(0, len(posts)):
        # Translates user UID to username
        name = UserCredentials.query.filter_by(uid=posts[i].user).first().username
        timePosted = posts[i].timePosted
        timePostedText = timePosted.strftime("%I:%M %p").lstrip('0') + " " + timePosted.strftime("%d %B, %Y")
        posts[i] = {"username": name, "timePostedText": timePostedText, "data": posts[i]}

    return render_template('homepage.html', username=session['username'], homepage_username=homepage_username,
                           posts=posts)


@app.route('/home')
def home_explicit():
    return redirect('/welcome')


@app.route('/iframes/iframe-post')
def iframe_post():
    return render_template('iframe-post.html')


@app.route('/create-post', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        if not request.form['text']:
            flash('Missing required fields', 'error')
        else:
            text = request.form['text']
            user = session['user-uid']
            timePosted = datetime.datetime.now()

            post_inst = UserPost(text=text, user=user, timePosted=timePosted)
            db.session.add(post_inst)
            db.session.commit()

            return redirect("/welcome")
    return render_template('create-post.html', username=session['username'])


if __name__ == '__main__':
    app.run(port=3001, host="localhost", debug=True)
