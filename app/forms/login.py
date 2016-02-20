from __future__ import unicode_literals
from wtforms import Form, StringField, PasswordField
from wtforms.validators import Required


class LoginForm(Form):
    username = StringField('username', [Required()])
    password = StringField('password', [Required()])
