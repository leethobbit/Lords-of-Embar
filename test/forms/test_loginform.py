from __future__ import unicode_literals
from webob.multidict import MultiDict
from robber import expect
from app.forms import LoginForm


def test_login_form_no_data():
    form = LoginForm(None)
    expect(form.validate()).to.be.false()

    form = LoginForm(MultiDict())
    expect(form.validate()).to.be.false()

def test_login_form_requires_password():
    form_data = MultiDict(
        username='savage'
    )
    form = LoginForm(form_data)
    expect(form.validate()).to.be.false()
    expect(form.errors).to.eq({
        'password': ['This field is required.']
    })

def test_login_form_requires_username():
    form_data = MultiDict(
        password='somepass'
    )
    form = LoginForm(form_data)
    expect(form.validate()).to.be.false()
    expect(form.errors).to.eq({
        'username': ['This field is required.']
    })

def test_login_form_is_okay():
    form_data = MultiDict(
        username='savage',
        password='somepass'
    )
    form = LoginForm(form_data)
    expect(form.validate()).to.be.true()
    expect(form.errors).to.eq({})
