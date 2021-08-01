from flask import Blueprint, url_for, render_template, redirect, session

import logic.user_logic as UserLogic

user_blueprint = Blueprint('users', __name__)


@user_blueprint.get('/login')
def login_get():
    return render_template('admin/../templates/user/login.html')


@user_blueprint.post('/login')
def login_post():
    UserLogic.login()
    return login_get()


@user_blueprint.get('/register')
def register_get():
    return render_template('admin/../templates/user/register.html')


@user_blueprint.post('/register')
def register_post():
    UserLogic.register()
    return register_get()


@user_blueprint.get('/change_password')
def change_password_get():
    return render_template('admin/../templates/user/change_password.html')


@user_blueprint.post('/change_password')
def change_password_post():
    UserLogic.change_password()
    return change_password_get()


@user_blueprint.get('/logout')
def logout():
    UserLogic.logout()
    return redirect(url_for('users.login_get'))



