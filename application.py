import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash

from extract import questions


# Ensure environment variable is set

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///urology.db")


@app.route("/")
def index():
    """index page"""
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    """registration page"""
    if request.method == 'GET':
        return render_template("register.html")

    elif request.method == 'POST':
        # Query database if hospno exists
        rows = db.execute("SELECT * FROM patients WHERE hospno = :hospno",
                          hospno=request.form.get("hospno"))
        if len(rows) > 0:
            return

        # Add patient to database
        session_id = db.execute("INSERT INTO 'patients' ('firstname', 'lastname','hospno','dob') VALUES (:firstname, :lastname,:hospno,:dob)", \
        firstname=request.form.get("firstname"), lastname=request.form.get("lastname"),\
        hospno=request.form.get("hospno"),dob=request.form.get("dob"))

        #save patient id for session
        session["user_id"] = session_id

        # Redirect user to home page
        return redirect("/")


@app.route("/eq5d5l", methods=["GET", "POST"])
def eq5d5l():
    """eq5d5l questionnaire page"""
    if request.method == 'GET':
        return render_template("eq5d5l.html")

@app.route("/iciqui", methods=["GET", "POST"])
def iciqui():
    """Display iciqui questionnaire"""
    if request.method == 'GET':
        return render_template("iciqui.html")

@app.route("/lutsqol", methods=["GET", "POST"])
def lutsqol():
    """Display lutsqol questionnaire"""
    if request.method == 'GET':
        return render_template("lutsqol.html",questionlist=questions)
