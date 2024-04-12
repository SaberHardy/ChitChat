from flask import Flask, render_template, request, redirect, url_for
from flask_login import current_user, login_required, LoginManager, login_user, logout_user
from flask_sqlalchemy import SQLAlchemy

from forms.forms import LoginForm
from models.models import UsersModel, db
from flask_wtf.csrf import CSRFProtect
from werkzeug.security import generate_password_hash, check_password_hash
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
import os

app = Flask(__name__, template_folder='templates')

app.config["SECRET_KEY"] = "another_secret_key"

UPLOAD_FOLDER = 'static/imgs/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:12345@localhost/chat_users"

login_manager = LoginManager()
login_manager.init_app(app)

db.init_app(app)

migrate = Migrate(app, db)


login_manager = LoginManager()
login_manager.init_app(app=app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return UsersModel.query.get(int(user_id))


@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        print('Login Successfully!!')

        user = UsersModel.query.filter_by(username=form.username.data).first()
        if user:
            # Check the hash
            if check_password_hash(user.password_hash, form.password.data):
                login_user(user)

                # flash("Login Succesfull!!")
                return redirect(url_for('all_users'))
            else:
                print('Wrong Password - Try Again!')
                # flash("Wrong Password - Try Again!")
        else:
            print("That User Doesn't Exist! Try Again...")
            # flash("That User Doesn't Exist! Try Again...")

    return render_template('chit_chat/login.html', form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    # flash("You Have Been Logged Out!")
    return redirect(url_for('/'))


@app.route('/welcome', methods=['GET', 'POST'])
def welcome():
    return render_template('chit_chat/welcome_page.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        name = request.form['name']
        password = request.form['password']
        repeat_password = request.form['repeat_password']

        if password != repeat_password:
            # Passwords don't match
            return render_template('chit_chat/register.html',
                                   error="Passwords don't match")

        # Check if the username or email already exists in the database
        existing_user = UsersModel.query.filter((UsersModel.username == username) | (UsersModel.email == email)).first()
        if existing_user:
            # User or email already exists
            return render_template('chit_chat/register.html',
                                   error="Username or email already exists")

        # Create a new user
        new_user = UsersModel(username=username,
                              email=email,
                              name=name,
                              password=password)

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))

    return render_template('chit_chat/register.html')


@app.route('/all_users', methods=['POST', 'GET'])
def all_users():
    all_us = UsersModel.query.all()
    return render_template('chit_chat/all_users.html', all_us=all_us)


if __name__ == '__main__':
    app.run()
