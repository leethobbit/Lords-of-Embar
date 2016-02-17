from sure import expect
from app.models import User


def test_user_initialize(testbed, server):
    user = User(username='foo', password='bar')
    user.put()
    expect(User.query().count()).to.equal(1)
