# all the imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("home.html")
	
@app.route("/about")
def about():
	return render_template("about.html")
	
@app.route("/contact")
def contact():
	return render_template("contact.html")

@app.route("/research")
def research():
	return render_template("research.html")

@app.route("/interests")
def interests():
	return render_template("interests.html")


if __name__ == '__main__':
    app.run()
