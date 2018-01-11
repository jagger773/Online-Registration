from flask import request, session, redirect, url_for , render_template
from passlib.handlers import bcrypt

from models import User
from app import app, db


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/post')
def post():
    return render_template('post.html')


@app.route('/register')
def register():
    return render_template('register')
