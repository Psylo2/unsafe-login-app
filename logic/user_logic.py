from flask import session, request, url_for, redirect, flash, render_template

from utils.valid_utils import LoginUtils, RegisterUtils
from models.user import User
from models.password import Password



def login():
    try:
        name_email = request.form['name_email']
        password = request.form['password']
        print("here",Password.find_one_by("pablo"))
        if LoginUtils._valid_login(name_email, password):
            user = User.find_from_db(name_email,)
            password = Password.find_one_by(user._name)
            print(user)
            print(password)
            if User.find_from_db(name_email,)\
                    and Password.find_one_by(User.find_from_db(name_email,)._name):
                        session['name_email'] = name_email
                        print("here")
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
            User(username, email, password, 0).save_to_db()
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



