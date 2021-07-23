from models.user import User, UserUtils
from flask import session, request, url_for, redirect


def login_name_is_valid(name_email: str) -> bool:
    return True if UserUtils.email_is_valid(name_email) or\
                   UserUtils.username_is_valid(name_email) else False


def login():
    try:
        name_email = request.form['name_email']
        password = request.form['password']
        if login_name_is_valid(name_email) and UserUtils.password_is_valid(password):

            if User.valid_login(name_email, password):
                session['name_email'] = name_email
                return redirect(url_for('home'))

    except Exception as e:
        print(e)


def logout():
    session['name_email'] = None
