from models.user import User, UserUtils
from flask import session, request, url_for, redirect


def login():
    try:
        username = request.form['username']
        password = request.form['password']
        if UserUtils.username_is_valid(username) and UserUtils.password_is_valid(password):
            if User.valid_login(username, password):
                session['username'] = username
                return redirect(url_for('home'))

    except Exception as e:
        print(e)


def logout():
    session['username'] = None
