from google.appengine.ext import ndb


class User(ndb.Model):
    """ Authentication class
    """
    username = ndb.StringProperty()
    password = ndb.StringProperty()
    date_created = ndb.DateTimeProperty(auto_now_add=True)
    date_updated = ndb.DateTimeProperty(auto_now=True)
