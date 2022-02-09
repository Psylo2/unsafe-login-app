from flask import Blueprint, url_for, render_template, redirect

user_blueprint = Blueprint('users', __name__)
user_blueprint.handler = None


@user_blueprint.get('/login')
def login_get():
    return render_template('user/login.html')


@user_blueprint.post('/login')
def login_post():
    try:
        result = user_blueprint.handler.login()
        if result:
            return redirect(url_for('home'))
        return login_get()

    except Exception:
        return login_get()


@user_blueprint.get('/register')
def register_get():
    return render_template('user/register.html')


@user_blueprint.post('/register')
def register_post():
    try:
        result = user_blueprint.handler.register()
        if result:
            return redirect(url_for('users.login_get'))
        return register_get()

    except Exception:
        return register_get()


@user_blueprint.get('/change_password')
def change_password_get():
    return render_template('user/change_password.html')


@user_blueprint.post('/change_password')
def change_password_post():
    try:
        result = user_blueprint.handler.change_password()
        if result:
            return redirect(url_for('home'))
        return change_password_get()

    except Exception:
        return change_password_get()


@user_blueprint.get('/logout')
def logout():
    try:
        user_blueprint.handler.logout()
        return redirect(url_for('users.login_get'))
    except Exception:
        return redirect(url_for('users.login_get'))
