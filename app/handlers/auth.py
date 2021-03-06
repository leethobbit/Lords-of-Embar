from __future__ import unicode_literals
from .base import BaseRequestHandler
from app.forms import RegisterForm, LoginForm
from app.models import User, UserAccess


class AuthRequestHandler(BaseRequestHandler):
    """ Register and Account Session Handler
        - user can register on the system
        - user can log in to the system
        - user can log out of the system
    """
    def post_register(self):
        form = RegisterForm(self.request.POST)

        if not form.validate():
            self.session.add_flash(form.errors, key='register_errors')
            return self.redirect('/')

        if User.exists(form.username.data):
            self.session.add_flash({
                'username': ['User with this username exists.']
            }, key='register_errors')
            return self.redirect('/')

        user = User.new(form.username.data,
                        form.password.data,
                        form.race.data)
        user.put()
        self.start_user_session(user)
        return self.redirect('/game/')

    def post_login(self):
        form = LoginForm(self.request.POST)
        errors = form.errors

        if form.validate():
            user = User.get_by_password(form.username.data, form.password.data)
            if user is None:
                errors = {'username': ['Invalid username or password.']}
            else:
                self.start_user_session(user)
                return self.redirect('/game/')

        self.session.add_flash(errors, key='login_errors')
        self.redirect('/')

    def get_logout(self):
        self.end_user_session()
        return self.redirect('/')
