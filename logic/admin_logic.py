from flask import session, request, url_for, redirect, flash
from models.password.password import Password


# def _password_complex(ups: str):#, lows: str, digits: str):#, special: str):  # , specials: str):
#     print(ups)
#     re = ""
#     if ups == "1":
#         re += "A-Z"
#     # if lows == "1":
#     #     re += "a-z"
#     # if digits == "1":
#     #     re += "0-9"
#     # if special == "1":
#     #     re += "\!\@\#\$\%\^\&\*\_\+\.\,"
#     print(re)

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

        Password._set_config(password_length,
                             re,
                             password_history,
                             use_dict,
                             password_tries)

    except Exception as e:
        print(e)
        flash('Invalid Inputs', 'danger')
    return redirect(url_for('admin.password_conf_get'))


def users_list():
    pass
