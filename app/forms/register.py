from __future__ import unicode_literals
from wtforms import Form, StringField, PasswordField
from wtforms.validators import Required, Email, EqualTo


class RegisterForm(Form):
    email = StringField('email', [
        Required(),
        Email(message='Requires valid email address.')
    ])
    username = StringField('username', [
        Required()
    ])
    password = PasswordField('password', [
        Required()
    ])
    passtest = PasswordField('passtest', [
        Required(),
        EqualTo('password', message='Passwords must match.')
    ])
