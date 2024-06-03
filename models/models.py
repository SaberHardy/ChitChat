from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, login_user, login_required

db = SQLAlchemy()


class UsersModel(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    name = db.Column(db.String(200), nullable=False)
    # another_name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password_hash = db.Column(db.String(255))
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    connected = db.Column(db.Boolean, default=False, nullable=False)

    @property
    def password(self):
        raise AttributeError('Password is not readable attribute!')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<Name %r>' % self.name


class MessagesModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('users_model.id'), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('users_model.id'), nullable=False)
    message_content = db.Column(db.Text, nullable=False)
    is_read = db.Column(db.Boolean, default=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    # Define relationships with the UsersModel
    sender = db.relationship('UsersModel', foreign_keys=[sender_id], backref='sent_messages')
    receiver = db.relationship('UsersModel', foreign_keys=[receiver_id], backref='received_messages')

    def __repr__(self):
        return f"<Message {self.id}>"
