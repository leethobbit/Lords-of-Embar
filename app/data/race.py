from __future__ import unicode_literals
from collections import namedtuple


TUPLE = namedtuple('Race', 'id name description offense defense casualty income covert sentry')

####
## Player Race
## - racial offensive modifier
## - racial defensive modifier
## - racial casualty modifier
## - racial income modifier
## - racial covert modifier
## - racial sentry modifier
###
RACES = frozenset([
    TUPLE('race-01', 'Human', 'humans are da best', 0, 0, 0, 0, 0, 0),
    TUPLE('race-02', 'Orc', 'Orcs drool', 0, 0, 0, 0, 0, 0),
])


def get_by_id(race_id):
    for each in RACES:
        if each.id == race_id:
            return each
    return None
