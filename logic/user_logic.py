from models.user import User, UserUtils
from flask import session, request, url_for, redirect, flash


def login_name_is_valid(name_email: str, password: str) -> bool:
    return True if (UserUtils.email_is_valid(name_email) or
                    UserUtils.username_is_valid(name_email)) and \
                   UserUtils.password_is_valid(password) else False


def register_is_valid(username: str, email: str, password: str, re_password: str) -> bool:
    return True if UserUtils.username_is_valid(username) and \
                   UserUtils.email_is_valid(email) and \
                   UserUtils.password_is_valid(password) and \
                   UserUtils.password_is_valid(re_password) else False


def login():
    try:
        name_email = request.form['name_email']
        password = request.form['password']
        if login_name_is_valid(name_email, password):
            if User.valid_login(name_email, password):
                session['name_email'] = name_email
                return redirect(url_for('home'))

    except Exception as e:
        print(e)


def register():
    try:
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        re_password = request.form['re_password']
        if register_is_valid(username, email, password, re_password):
            User(username, email, password).save_to_db()
            return redirect(url_for('users.login_get'))

    except:
        flash('Invalid Inputs', 'danger')
        return redirect(url_for('users.register_get'))


def logout():
    session['name_email'] = None
