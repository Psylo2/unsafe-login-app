from flask import Flask, render_template, request
import json

from views.users import user_blueprint
from views.admins import admin_blueprint

app = Flask(__name__)

app.secret_key = "Secret_Key"
app.config.update(ADMIN="Admin")

@app.get('/')
def home():
    return render_template('home.html')

app.register_blueprint(user_blueprint,
                       url_prefix="/users")

app.register_blueprint(admin_blueprint,
                       url_prefix="/admin")

if __name__ == '__main__':
    app.run(port=5000, debug=True)
