from __future__ import unicode_literals
from google.appengine.ext import ndb
from webapp2_extras import security

from .structures.user_profile import UserProfile


def hash_password(prop, value):
    return security.generate_password_hash(value)


class User(ndb.Model):
    """ Authentication class
        - stores account credentials
        - stores game related bonuses
          - technologies
        - stores game related metadata
          - race
          - gold and turns
    """
    email = ndb.StringProperty(required=True, indexed=False)
    username = ndb.StringProperty(required=True, indexed=False)
    password = ndb.StringProperty(required=True, indexed=False, validator=hash_password)
    date_created = ndb.DateTimeProperty(auto_now_add=True)
    date_updated = ndb.DateTimeProperty(auto_now=True)

    profile = ndb.LocalStructuredProperty(UserProfile, required=True)

    email_lc = ndb.ComputedProperty(lambda self: self.email.lower())
    username_lc = ndb.ComputedProperty(lambda self: self.username.lower())

    @classmethod
    def get_by_password(cls, username, password):
        user = cls.query(cls.username_lc == username.lower()).get()
        if user is not None and user.check_password(password):
            return user
        return None

    @classmethod
    def exists(cls, email, username):
        query = ndb.OR(cls.email_lc == email.lower(),
                       cls.username_lc == username.lower())
        return cls.query(query).count() > 0

    @classmethod
    def new(cls, email, username, password, race):
        return cls(email=email,
                   username=username,
                   password=password,
                   profile=UserProfile(race_id=race))

    def check_password(self, password):
        return security.check_password_hash(password, self.password)
