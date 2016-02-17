from __future__ import unicode_literals
from collections import namedtuple


TUPLE = namedtuple('Race', 'id name description offense defense casualty income')


RACES = frozenset([
    TUPLE('race-1', 'Human', 'humans are da best', 0, 0, 0, 0),
])


def get_by_id(race_id):
    for each in RACES:
        if each.id == race_id:
            return each
    return None
