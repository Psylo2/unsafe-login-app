from flask import session, request, url_for, redirect, flash, render_template

from utils.user_utils import LoginUtils, RegisterUtils
from models.user import User


def login():
    try:
        name_email = request.form['name_email']
        password = request.form['password']
        if LoginUtils._valid_login(name_email, password):
            if User.valid_login(name_email, password):
                session['name_email'] = name_email
                return redirect(url_for('home'))

    except Exception as e:
        print(e)
        flash('Invalid Inputs', 'danger')
        return redirect(url_for('users.login_get'))


def register():
    try:
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        re_password = request.form['re_password']
        if RegisterUtils._valid_register(username, email, password, re_password):
            User(username, email, password).save_to_db()
        return redirect(url_for('users.login_get'))

    except Exception as e:
        print(e)
        flash('Invalid Inputs', 'danger')
        return redirect(url_for('users.register_get'))


def change_password():
    try:
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        re_password = request.form['re_password']
        if RegisterUtils._valid_register(username, email, password, re_password):
            user = User.find_from_db(username)
            user._password = password
            user.update_password()
        return redirect(url_for('home'))

    except Exception as e:
        print(e)
        flash('Invalid Inputs', 'danger')
        return redirect(url_for('users.change_password_get'))


def logout():
    session['name_email'] = None


def users_list():
    _users = User.find_many_by()
    session['block_user'] = None
    return render_template('password/user_list.html', users=_users)

def block_user():
    User.find_from_db(session['block_user']).block_user_model()

    return redirect(url_for('users.all_users_get'))

def unblock_user():
    print(session['block_user'])
    User.find_from_db(session['block_user']).unblock_user_model()
    return redirect(url_for('users.all_users_get'))
