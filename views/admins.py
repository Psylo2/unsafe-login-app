from flask import Blueprint, url_for, render_template, redirect

from models.user import UserLogic, requires_login

admin_blueprint = Blueprint('admin', __name__)


# @admin_blueprint.get('/all_users')
# def all_users_get():
#     return render_template('admin/all_users.html')