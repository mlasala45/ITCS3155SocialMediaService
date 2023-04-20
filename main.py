from flask import Flask, flash, redirect, url_for, render_template, session
from flask import request

from flask_sqlalchemy import SQLAlchemy

from db.db_connect import DB_HOST, DB_NAME, DB_USERNAME, DB_PASSWORD

# DB_HOST = "localhost"
# DB_NAME = "sandwich_maker"
# DB_USERNAME = "root"
# DB_Password = "root"

database_file = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:3306/{DB_NAME}"

app = Flask(__name__)
app.secret_key = "mysecret"
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)


class UserCredentials(db.Model):
    __tablename__ = 'user_credentials'
    uid = db.Column(db.Int(), primary_key=True, nullable=False)
    username = db.Column(db.String(36), nullable=False)
    password = db.Column(db.String(20), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password


class UserPost(db.Model):
    __tablename__ = 'user_posts'
    user = db.Column(db.Integer(), nullable=False)
    timePosted = db.Column(db.String(20), nullable=False)
    text = db.Column(db.String(280), nullable=False)

    def __init__(self, text):
        self.text = text


@app.route("/")
def home():
    return redirect("/login")


# Logs the user in. Called after details are validated. Returns false if an error occurred.
def log_user_in(username):
    session['username'] = username
    return True


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
                succ = log_user_in(username)
                if succ:
                    flash('Login successful', 'success')
                    return redirect("/welcome")
                else:
                    flash('Unknown error while logging in', category="error")
            else:
                flash("Incorrect password", category="error")
    return render_template('login.html')


@app.route('/welcome', methods=['GET'])
def welcome():
    return render_template('welcome.html', username=session['username'])

if __name__ == '__main__':
    app.run(port=3001, host="localhost", debug=True)
