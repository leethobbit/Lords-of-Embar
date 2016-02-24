from __future__ import unicode_literals
from collections import namedtuple


TUPLE = namedtuple('Race', 'id label description offense defense casualty income covert sentry')

####
## Player Race
## - racial offensive modifier
## - racial defensive modifier
## - racial casualty modifier
## - racial income modifier
## - racial covert modifier
## - racial sentry modifier
###
RACES = ([
    TUPLE('race-01', 'Humans',
            'Diplomacy and economics are keys to great fortune',
            0, 0, 0, 1.30, 1.35, 0),
    TUPLE('race-02', 'Dwarves',
            'Life in the mountains made them strong and rich',
            0, 1.40, 0, 1.15, 0, 0),
    TUPLE('race-03', 'Elves',
            'Cloaked in nature the elves strike fast and true',
            0, 0, 0.30, 0, 1.45, 0),
    TUPLE('race-04', 'Orcs',
            'Overpower your foes with the raw srength of the orcs',
            1.35, 1.20, 0, 0, 0, 0),
    TUPLE('race-05', 'Undead',
            'They were here before, they will be here after',
            0, 0, 0.15, 0, 0, 1.35)
])

IDS = [race.id for race in RACES]

def get_by_id(race_id):
    for each in RACES:
        if each.id == race_id:
            return each
    return None
