from __future__ import unicode_literals
import functools, logging
from webapp2 import RequestHandler, cached_property
from webapp2_extras import json, jinja2, sessions
from app.models import User


def requires_login(fn):
    @functools.wraps(fn)
    def f(self, *args, **kwds):
        if 'user' in self.session:
            return fn(self, *a)
        return self.abort(403)
    return f


class BaseRequestHandler(RequestHandler):
    """ Application Request Handler
        - supports json response
        - supports html response via jinja2 templates
        - supports model serialization
        - supports model collection serialization
    """
    def dispatch(self):
        self.session_store = sessions.get_store(request=self.request)
        try:
            RequestHandler.dispatch(self)
        finally:
            self.session_store.save_sessions(self.response)

    @cached_property
    def session(self):
        return self.session_store.get_session()

    @cached_property
    def jinja2(self):
        jinja2.default_config.update(
            template_path=self.app.config.get('template_path', 'templates')
        )
        return jinja2.get_jinja2(app=self.app)

    def json_view(self, content=None, **kwds):
        content = content or kwds
        self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
        self.response.write(json.encode(content))

    def html_view(self, template, context=None, **kwds):
        content = self.jinja2.render_template(template, **(context or kwds))
        self.response.headers['Content-Type'] = 'text/html; charset=utf-8'
        self.response.write(content)

    def start_user_session(self, user):
        if type(user) is User and user.key:
            self.session['user'] = user.key.urlsafe()

    def end_user_session(self):
        if 'user' in self.session:
            del self.session['user']

    def get_user_from_session(self):
        user_key = self.session.get('user', None)
        if user_key is not None:
            user = ndb.Key(urlsafe=self.session).get()
            if user is not None:
                return user
        self.abort(403)
