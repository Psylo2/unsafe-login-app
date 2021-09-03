from flask import request, url_for, redirect, flash, render_template
from models.user import User
from models.password import PasswordConfig


def users_list():
    _users = User.find_all_from_db()
    return render_template('admin/user_list.html', users=_users)


def block_user(block):
    user = User.find_from_db(block)
    user.block_user_model()


def unblock_user(unblock):
    user = User.find_from_db(unblock)
    user.unblock_user_model()


def password_configuration():
    re = ""
    try:
        try:
            re += "A-Z" if request.form['upper'] == "1" else ""
        except:
            pass
        try:
            re += "a-z" if request.form['lower'] == "1" else ""
        except:
            pass
        try:
            re += "0-9" if request.form['digits'] == "1" else ""
        except:
            pass
        try:
            re += "\!\#\$\%\^\&\*\_\+\.\," if request.form['spec'] == "1" else ""
        except:
            pass
        try:
            use_dict = True if request.form['use_dict'] == "1" else False
        except:
            use_dict = False

        password_length = request.form['length']
        password_history = request.form['history']
        password_tries = request.form['tries']

        PasswordConfig._set_config(length=password_length,
                             regex=re,
                             history=password_history,
                             dictionary=use_dict,
                             tries=password_tries)
        
        flash('Password Configuration Changed!', 'danger')

    except Exception as e:
        print(e)
        flash('Invalid Inputs', 'danger')
    return redirect(url_for('admin.password_conf_get'))
