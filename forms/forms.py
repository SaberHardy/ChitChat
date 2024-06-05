from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField("User Name", validators=[DataRequired()])
    password = PasswordField("Enter your Password!", validators=[DataRequired()])
    submit = SubmitField("Submit")


class UserForm(FlaskForm):
    username = StringField("username", )
    name = StringField("name", )
    phone_number = StringField("phone_number", )
    city = StringField("city", )
    street = StringField("street", )
    email = StringField("email", )
    submit = SubmitField("Submit")
