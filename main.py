from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from models.models import UsersModel, db
from flask_wtf.csrf import CSRFProtect
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
import os

app = Flask(__name__, template_folder='templates')

app.config["SECRET_KEY"] = "another_secret_key"

UPLOAD_FOLDER = 'static/imgs/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:12345@localhost/chat_users"

db.init_app(app)

migrate = Migrate(app, db)


@app.route('/', methods=['GET', 'POST'])
def login_user():
    return render_template('chit_chat/login.html')


@app.route('/welcome', methods=['GET', 'POST'])
def welcome():
    return render_template('chit_chat/welcome_page.html')


@app.route('/add_user', methods=['GET', 'POST'])
def register():
    return render_template('chit_chat/register.html')


if __name__ == '__main__':
    app.run()
