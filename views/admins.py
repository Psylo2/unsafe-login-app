from flask import Blueprint, render_template, redirect, url_for, flash

admin_blueprint = Blueprint('admin', __name__)
admin_blueprint.handler = None


@admin_blueprint.get('/password_config')
def password_conf_get():
    return render_template('admin/password_config.html')


@admin_blueprint.post('/password_config')
def password_conf_post():
    try:
        admin_blueprint.handler.password_configuration()
    except Exception:
        flash("Error occurred", 'danger')
    finally:
        return password_conf_get()


@admin_blueprint.get('/menu')
def menu_get():
    return render_template('admin/menu.html')


@admin_blueprint.get('/all_users')
def all_users_get():
    try:
        user_list = admin_blueprint.handler.users_list()
        return render_template('admin/user_list.html', users=user_list)
    except Exception:
        flash("Error occurred", 'danger')
        return menu_get()


@admin_blueprint.get('/block/<string:block>')
def block_user(block):
    try:
        admin_blueprint.handler.block_user(block)
        return redirect(url_for('admin.all_users_get'))
    except Exception:
        flash("Error occurred", 'danger')
        return menu_get()


@admin_blueprint.get('/unblock/<string:unblock>')
def unblock_user(unblock):
    try:
        admin_blueprint.handler.unblock_user(unblock)
        return redirect(url_for('admin.all_users_get'))
    except Exception:
        flash("Error occurred", 'danger')
        return menu_get()
