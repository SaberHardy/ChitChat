from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.fields.choices import SelectField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    username = StringField("User Name", validators=[DataRequired()])
    password = PasswordField("Enter your Password!", validators=[DataRequired()])
    submit = SubmitField("Submit")


class UserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    phone_number = StringField('Phone Number', validators=[DataRequired()])
    street = StringField('Street', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    # connected = SelectField('Status', choices=[('online', 'Online'), ('offline', 'Offline')])
    connected = SelectField('Status', choices=[(True, 'Online'), (False, 'Offline')], coerce=lambda x: x == 'True')
    submit = SubmitField('Submit')
