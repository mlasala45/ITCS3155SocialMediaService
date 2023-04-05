from flask import Flask, flash, redirect, url_for, render_template, session
from flask import request

from flask_sqlalchemy import SQLAlchemy

from db/db_connect import DB_HOST, DB_NAME, DB_USERNAME, DB_PASSWORD,

# DB_HOST = "localhost"
# DB_NAME = "sandwich_maker"
# DB_USERNAME = "root"
# DB_Password = "root"

database_file = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:3306/{DB_NAME}"

app = Flask(__name__)
app.secret_key = "mysecret"
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)


@app.route("/")
def home():
    return render_template("login.html")

if __name__ == '__main__':
    app.run(port=3001, host="localhost", debug=True)
