from google.appengine.ext import ndb
from app.data import race, tech


class UserProfile(ndb.Model):
    """ Represents a User's Game Profile
    """
    race_id = ndb.StringProperty(required=True, choices=race.IDS)
    gold =    ndb.IntegerProperty(default=50)
    turns =   ndb.IntegerProperty(default=0)

    offensive_tech_id = ndb.StringProperty(choices=tech.OFF_IDS, default=tech.OFF_IDS[0])
    defensive_tech_id = ndb.StringProperty(choices=tech.DEF_IDS, default=tech.DEF_IDS[0])
    economy_tech_id   = ndb.StringProperty(choices=tech.ECO_IDS, default=tech.ECO_IDS[0])
    sentry_tech_id    = ndb.StringProperty(choices=tech.STY_IDS, default=tech.STY_IDS[0])
    spy_tech_id       = ndb.StringProperty(choices=tech.SPY_IDS, default=tech.SPY_IDS[0])

    @property
    def race(self):
        return race.get_by_id(self.race_id)
