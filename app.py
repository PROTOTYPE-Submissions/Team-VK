from flask import Flask, render_template , request , redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def success():

	return render_template('index.html')


@app.route('/login',methods=['GET', 'POST'])
def login():
	return render_template("login.html")

@app.route('/courses',methods=['GET', 'POST'])
def courses():
	return render_template("courses.html")

@app.route('/index',methods=['GET', 'POST'])
def index():
	return redirect('/')


@app.route('/contact',methods=['GET', 'POST'])
def contact():
	return render_template('contact.html')

@app.route('/about',methods=['GET', 'POST'])
def about():
	return render_template('about.html')

@app.route('/courses',methods=['GET', 'POST'])
def enroll():
	return render_template('courses.html')


if __name__ == '__main__':
	app.run(debug=True)
  