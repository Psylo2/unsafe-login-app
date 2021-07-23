from flask import Blueprint, url_for, render_template, redirect

from models.user import UserLogic, requires_login

user_blueprint = Blueprint('users', __name__)


@user_blueprint.get('/login')
def login_get():
    return render_template('user/login.html')


@user_blueprint.post('/login')
def login_post():
    UserLogic.login()
    return login_get()


@user_blueprint.get('/logout')
def logout():
    UserLogic.logout()
    return redirect(url_for('users.login_get'))
