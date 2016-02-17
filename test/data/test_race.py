from robber import expect, BadExpectation
from app.data import race


def test_get_by_id_when_exists_returns_race():
    r = race.get_by_id('race-1')

    expect(r).to.be.a.tuple()
    expect(r.id).to.eq('race-1')
    expect(r.name).to.eq('Human')

def test_get_by_id_when_not_exists_returns_None():
    r = race.get_by_id('race-noexist')

    expect(r).to.be.none()

def test_get_by_id_when_invalid_id_returns_None():
    r = race.get_by_id(5)
    
    expect(r).to.be.none()
