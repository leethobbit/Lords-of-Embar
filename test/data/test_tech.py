from robber import expect, BadExpectation
from app.data import tech

def test_get_by_id_when_exists_returns_tech():
    t = tech.get_by_id('tech-siege-01')

    expect(t).to.be.a.tuple()
    expect(t.id).to.eq('tech-siege-01')
    expect(t.name).to.eq('None')

def test_get_by_id_when_not_exists_returns_None():
    t = tech.get_by_id('tech-noexist')

    expect(t).to.be.none()

def test_get_by_id_when_invalid_id_returns_None():
    t = tech.get_by_id(5)

    expect(t).to.be.none()

def test_get_upgrade_when_exists_returns_tech():
    t = tech.get_upgrade('tech-siege-01')

    expect(t).to.be.a.tuple()
    expect(t.id).to.eq('tech-siege-02')
    expect(t.name).to.eq('Flaming Arrows')

def test_get_upgrade_when_at_limit_returns_None():
    t1 = tech.SIEGE_TECH[-1]
    t2 = tech.get_upgrade(t1.id)

    expect(t2).to.be.none()
