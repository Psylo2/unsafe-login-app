from flask import Blueprint, url_for, render_template, redirect

from models.password import AdminLogic

admin_blueprint = Blueprint('admin', __name__)



@admin_blueprint.get('/password_config')
def password_conf_get():
    return render_template('password/password_config.html')


@admin_blueprint.post('/password_config')
def password_conf_post():
    AdminLogic.password_configuration()
    return password_conf_get()


