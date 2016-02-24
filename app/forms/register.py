from __future__ import unicode_literals
from wtforms import Form, StringField, PasswordField
from wtforms.validators import Required, Email, EqualTo, AnyOf

from app.data import race


class RegisterForm(Form):
    race = StringField('race', [
        Required(), AnyOf(race.IDS)
    ])
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
