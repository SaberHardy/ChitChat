from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required, LoginManager, login_user, logout_user

from forms.forms import LoginForm, UserForm
from models.models import UsersModel, db  # , MessagesModel
from werkzeug.security import check_password_hash
from flask_migrate import Migrate

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
                return redirect(url_for('welcome'))
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
    return redirect(url_for('login'))


@app.route('/welcome', methods=['GET', 'POST'])
def welcome():
    all_users = UsersModel.query.all()
    return render_template('chit_chat/welcome_page.html', all_users=all_users)


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


# @app.route('/send_message', methods=['POST'])
# @login_required
# def send_message():
#     sender_id = current_user.id
#     receiver_id = request.form['receiver_id']
#     message_content = request.form['message_content']
#
#     new_message = MessagesModel(sender_id=sender_id,
#                                 receiver_id=receiver_id,
#                                 message_content=message_content)
#
#     db.session.add(new_message)
#     db.session.commit()
#
#     # Optionally, send real-time notification to the receiver
#
#     return redirect(url_for('chat_with_users'))
#
#
# @app.route('/get_messages/<int:receiver_id>', methods=['GET'])
# @login_required
# def get_messages(receiver_id):
#     messages = MessagesModel.query.filter(
#         ((MessagesModel.sender_id == current_user.id) & (MessagesModel.receiver_id == receiver_id)) |
#         ((MessagesModel.sender_id == receiver_id) & (MessagesModel.receiver_id == current_user.id))
#     ).order_by(MessagesModel.timestamp).all()
#
#     # Optionally, mark messages as read
#
#     return render_template('chit_chat/messages.html', messages=messages)

@app.route('/chat_users', methods=['POST', 'GET'])
def chat_users():
    users = UsersModel.query.all()
    return render_template('chit_chat/chat_users.html', users=users)


@app.route('/user_details/<int:user_id>', methods=['POST', 'GET'])
def user_profile(user_id):
    user = UsersModel.query.get_or_404(user_id)
    return render_template('chit_chat/user_profile.html', user=user)


@app.route('/update_user/<int:user_id>', methods=['POST', 'GET'])
def update_user_profile(user_id):
    form = UserForm()
    user_to_update = UsersModel.query.get_or_404(user_id)

    if request.method == "POST":
        user_to_update.username = request.form['username']
        user_to_update.name = form.name.data
        user_to_update.phone_number = request.form['phone_number']
        user_to_update.city = request.form['city']
        user_to_update.street = request.form['street']
        user_to_update.email = request.form['email']
        user_to_update.connected = form.connected.data

        try:
            db.session.commit()
            flash("User updated successfully!")
            return redirect(url_for('welcome'))
        except:
            flash("The User didn't update successfully!")
            return render_template("chit_chat/update_user.html", form=form, user_to_update=user_to_update)

    return render_template("chit_chat/update_user.html", form=form, user_to_update=user_to_update)


if __name__ == '__main__':
    app.run()
