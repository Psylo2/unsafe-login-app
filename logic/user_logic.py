from flask import session, request, url_for, redirect, flash, render_template

from utils.valid_utils import LoginUtils, RegisterUtils
from models.user import User
from models.password import Password



def login():
    try:
        name_email = request.form['name_email']
        password = request.form['password']
        
        if LoginUtils._valid_login(name_email, password):
            user = User.find_from_db(name_email)
            password = Password.find_one_by(user._name)
            if user and password.password_match(password):
                session['name_email'] = name_email
                flash(f'Welcome {user,_name}', 'danger')

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

        if RegisterUtils._valid_register(username, email,
                                         password, re_password):
            user = User(username, email,0)
            user.save_to_db()
            Password(username=user._name).save_to_db()
            flash('Registration Succsess!', 'danger')
    
            
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
        
        if RegisterUtils._valid_register(username, email,
                                         password, re_password):
            user = User.find_from_db(username)
            if user:
                new_passw = Password(username=username)
                if new_passw.confirm_password(user._name, password):
                    new_order = new_passw.order_new_password(
                        username=user._name,
                        password=password)
                    new_passw.update_to_db(new_order)
                    flash('Password Changed!', 'danger')
        return redirect(url_for('home'))

    except Exception as e:
        print(e)
        flash('Invalid Inputs', 'danger')
        return redirect(url_for('users.change_password_get'))


def logout():
    flash('Farwell', 'danger')
    session['name_email'] = None



