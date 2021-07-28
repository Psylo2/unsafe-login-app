from flask import request, url_for, redirect, flash
from models.password.password import Password


def password_configuration():
    try:
        password_length = request.form['length']

        re = ""
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

        password_history = request.form['history']

        try:
            use_dict = True if request.form['use_dict'] == "1" else False
        except:
            use_dict = False

        password_tries = request.form['tries']

        Password._set_config(self=Password,
                             length=password_length,
                             regex=re,
                             history=password_history,
                             dictionary=use_dict,
                             tries=password_tries)

    except Exception as e:
        print(e)
        flash('Invalid Inputs', 'danger')
    return redirect(url_for('admin.password_conf_get'))

