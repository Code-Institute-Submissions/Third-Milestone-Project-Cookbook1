from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField, validators
from wtforms.validators import Length, EqualTo, DataRequired


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=5, max=15)])
    password = PasswordField('Password',
                             validators=[DataRequired(),
                                         Length(min=5, max=15)])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(),
                                                 EqualTo('password', message='Passwords should match')])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(),
                                       Length(min=5, max=15)])
    password = PasswordField('Password',
                             validators=[DataRequired(),
                                         Length(min=5, max=15)])
    remember_user = BooleanField('Stay Logged In')
    submit = SubmitField('Login')
