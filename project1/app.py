import os
import requests
from flask import Flask, request, session, render_template, flash, redirect, url_for
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from forms import RegistrationForm, LoginForm, SearchForm
from passlib.hash import pbkdf2_sha256

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    os.environ["DATABASE_URL"] = "postgres://jnhdylhrgoontf:bd8b68d76e81fb5b9c7489e2ceddb041320d600a613a19aa45da1aa58697e493@ec2-54-243-208-234.compute-1.amazonaws.com:5432/d61cotnr4krl5v"

if not os.getenv('FLASK_CONFIG'):
    os.environ['FLASK_CONFIG'] = 'dev'


proxies = dict(http='socks5h://127.0.0.1:6005',
               https='socks5h://127.0.0.1:6005')

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))
# res = requests.get("https://www.goodreads.com/book/review_counts.json",
#                   params={"key": "UnJEUENuYcvAB9ZAWrD7Q", "isbns": "9781324002642"}, proxies=proxies)

users = {}
posts = []


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():

        username = form.username.data
        password = form.password.data
        hash = pbkdf2_sha256.hash(password)

        db.execute("INSERT INTO users (username, password) VALUES (:name, :hash)",
                   {"name": username, "hash": hash})
        db.commit()

        flash(f'Account created for {form.username.data}!', 'sucess')

        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form=form)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = request.form.get("username")
        password = request.form.get("password")
        res = db.execute("SELECT id, password FROM users WHERE username LIKE :name", {
            "name": username}).fetchone()
        db_hash = res.password
        user_id = res.id
        if pbkdf2_sha256.verify(password, db_hash):
            session["logged_in"] = True
            session["user_id"] = user_id
            session["user_name"] = username
            return redirect(url_for('search'), "303")
        else:
            flash("Invalid password")
            return redirect(url_for('login'), "303")
    return render_template('login.html', title='login', form=form)


@app.route('/logout')
def logout():
    if session["logged_in"] == True:
        session["logged_in"] = False
        session["user_id"] = None
        flash("Logout successful")
    return redirect(url_for('home'), "303")


@app.route("/search", methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if session["logged_in"] == True:
        if form.validate_on_submit():
            isbn = request.form.get("isbn")
            res = db.execute(
                "SELECT * FROM books WHERE isbn LIKE :isbn", {"isbn": isbn}).fetchone()
            if res:
                if res['isbn']:
                    review = requests.get("https://www.goodreads.com/book/review_counts.json",
                                          params={"key": "UnJEUENuYcvAB9ZAWrD7Q", "isbns": isbn}, proxies=proxies)
                    review = review.json()
                    return render_template('search.html', title='search', form=form, res=res, review=review)
                return render_template('search.html', title='search', form=form)
            flash('not found')
        return render_template('search.html', title='search', form=form)
    return render_template('home.html')
