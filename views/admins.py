from flask import Blueprint, render_template, redirect, url_for
import logic.admin_logic as AdminLogic

admin_blueprint = Blueprint('admin', __name__)

@admin_blueprint.get('/password_config')
def password_conf_get():
    return render_template('admin/password_config.html')


@admin_blueprint.post('/password_config')
def password_conf_post():
    AdminLogic.password_configuration()
    return password_conf_get()

@admin_blueprint.get('/menu')
def menu_get():
    return render_template('admin/menu.html')


@admin_blueprint.get('/all_users')
def all_users_get():
    return AdminLogic.users_list()


@admin_blueprint.get('/block/<string:block>')
def block_user(block):
    AdminLogic.block_user(block)
    return redirect(url_for('admin.all_users_get'))


@admin_blueprint.get('/unblock/<string:unblock>')
def unblock_user(unblock):
    AdminLogic.unblock_user(unblock)
    return redirect(url_for('admin.all_users_get'))
