from flask import Flask, render_template

from app_configurration import AppConfiguration

from views.users import user_blueprint
from views.admins import admin_blueprint

from logic import UserLogic, AdminLogic

app = Flask(__name__)
AppConfiguration(app=app)


@app.get('/')
def home():
    return render_template('home.html')


user_blueprint.handler = UserLogic()
admin_blueprint.handler = AdminLogic()

app.register_blueprint(blueprint=user_blueprint,
                       url_prefix="/users")

app.register_blueprint(blueprint=admin_blueprint,
                       url_prefix="/admin")

if __name__ == '__main__':
    app.run(port=5000, debug=False)
