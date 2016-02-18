from __future__ import unicode_literals
from collections import namedtuple


TECH = namedtuple('Tech', 'id name price modifier description')


SIEGE_TECH = (
    TECH('tech-siege-01', 'None'           ,          0 , 1.000 , ''),
    TECH('tech-siege-02', 'Flaming Arrows' ,      40000 , 1.333 , ''),
    TECH('tech-siege-03', 'Ballistas'      ,      80000 , 1.667 , ''),
    TECH('tech-siege-04', 'Battering Ram'  ,     160000 , 2.000 , ''),
    TECH('tech-siege-05', 'Ladders'        ,     320000 , 2.333 , ''),
    TECH('tech-siege-06', 'Trojan Horse'   ,     640000 , 2.667 , ''),
)

FORT_TECH = (
    TECH('tech-fort-01', 'Camp'            ,          0 , 1.000 , ''),
    TECH('tech-fort-02', 'Stockade'        ,      40000 , 1.250 , ''),
    TECH('tech-fort-03', 'Rabid Pitbulls'  ,      80000 , 1.500 , ''),
    TECH('tech-fort-04', 'Walled Town'     ,     160000 , 1.750 , ''),
    TECH('tech-fort-05', 'Towers'          ,     320000 , 2.000 , ''),
    TECH('tech-fort-06', 'Battlements'     ,     640000 , 2.250 , ''),
)

ECON_TECH = (
    TECH('tech-econ-01', 'None'            ,          0 , 1.000 , ''),
)

SPY_TECH = (
    TECH('tech-spy-01',  'None'            ,          0 , 1.000 , ''),
)

SENTRY_TECH = (
    TECH('tech-sentry-01', 'None'          ,          0 , 1.000 , ''),
)


COMBINED = SIEGE_TECH + FORT_TECH + ECON_TECH + SPY_TECH + SENTRY_TECH


def get_by_id(tech_id):
    for each in COMBINED:
        if each.id == tech_id:
            return each
    return None

def get_upgrade(tech_id):
    if tech_id.startswith('tech-siege'):
        group = iter(SIEGE_TECH)
    elif tech_id.startswith('tech-fort'):
        group = iter(FORT_TECH)
    else:
        raise NotImplementedError

    try:
        for tech in group:
            if tech.id == tech_id:
                return next(group)
    except StopIteration:
        pass

    return None
