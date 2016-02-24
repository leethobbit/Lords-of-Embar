from __future__ import unicode_literals
from webob.multidict import MultiDict
from robber import expect
from app.forms import RegisterForm


def test_register_form_no_data():
    form = RegisterForm(None)
    expect(form.validate()).to.be.false()

    form = RegisterForm(MultiDict())
    expect(form.validate()).to.be.false()

def test_register_form_partial_is_invalid():
    form_data = MultiDict(
        email='test@test.com',
        username='savage',
        password='somepass'
    )
    form = RegisterForm(form_data)
    expect(form.validate()).to.be.false()
    expect(form.errors).to.eq({
        'passtest': ['This field is required.'],
        'race': ['This field is required.']
    })

def test_register_form_requires_email():
    form_data = MultiDict(
        race='race-01',
        email='ausername',
        username='savage',
        password='somepass',
        passtest='somepass'
    )
    form = RegisterForm(form_data)
    expect(form.validate()).to.be.false()
    expect(form.errors).to.eq({
        'email': ['Requires valid email address.']
    })

def test_register_form_requires_valid_race():
    form_data = MultiDict(
        race='race-does-not-exist',
        email='test@test.com',
        username='savage',
        password='somepass',
        passtest='somepass'
    )
    form = RegisterForm(form_data)
    expect(form.validate()).to.be.false()
    expect(form.errors).to.eq({
        'race': ['Invalid value, must be one of: race-01, race-02.']
    })

def test_register_form_passwords_must_match():
    form_data = MultiDict(
        race='race-01',
        email='test@test.com',
        username='savage',
        password='somepass',
        passtest='badpass'
    )
    form = RegisterForm(form_data)
    expect(form.validate()).to.be.false()
    expect(form.errors).to.eq({
        'passtest': ['Passwords must match.']
    })

def test_register_form_is_okay():
    form_data = MultiDict(
        race='race-01',
        email='test@test.com',
        username='savage',
        password='somepass',
        passtest='somepass'
    )
    form = RegisterForm(form_data)
    expect(form.validate()).to.be.true()
    expect(form.errors).to.eq({})
