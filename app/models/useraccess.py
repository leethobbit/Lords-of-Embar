from google.appengine.ext import ndb


class UserAccess(ndb.Model):
    ip_address = ndb.StringProperty(required=True)
    date_created = ndb.DateTimeProperty(auto_now_add=True)
