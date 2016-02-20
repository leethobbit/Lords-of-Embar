from __future__ import unicode_literals
from robber import expect
from app.models import User


def test_user_initialize(testbed):
    user = User(email='TEST@test.com', username='Foo', password='bar')
    expect(user.email).to.eq('TEST@test.com')
    expect(user.email_lc).to.eq('test@test.com')
    expect(user.username).to.eq('Foo')
    expect(user.username_lc).to.eq('foo')
    expect(user.password).to.not_eq('bar')
    expect(user.check_password('bar')).to.be.true()
    password = user.password

    user.put()

    expect(User.query().count()).to.equal(1)
    expect(User.query().get().password).to.eq(password)

def test_get_by_password(testbed):
    User(email='TEST@test.com', username='Foo', password='Bazaar').put()
    expect(User.query().count()).to.equal(1)
    expect(User.query().get().password).to.not_eq('Bazaar')

    user = User.get_by_password('Foo', 'Bazaar')
    expect(user is not None).to.be.true()
    expect(user.password).to.not_eq('Bazaar')
