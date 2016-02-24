from __future__ import unicode_literals
from robber import expect
from google.appengine.ext import ndb
from app.models import User


get_fixture = lambda: {
    'race': 'race-01',
    'username': 'embar-TEST',
    'password': 'somepass',
    'passtest': 'somepass'
}


def test_register_when_valid_creates_user(testbed, server):
    response = server.post('/auth/register', get_fixture())

    expect(response.status).to.eq('302 Moved Temporarily')
    expect(response.status_int).to.eq(302)
    expect(response.headers['Location']).to.eq('http://localhost/game/')

    user = User.query().get()
    expect(user.username).to.eq('embar-TEST')
    expect(user.username_lc).to.eq('embar-test')
    expect(user.password).to.not_eq('somepass')

def test_register_when_invalid_form_redirects_to_index(testbed, server):
    fixture = get_fixture().copy()
    fixture['passtest'] = 'blargh'
    response = server.post('/auth/register', fixture)

    expect(response.status).to.eq('302 Moved Temporarily')
    expect(response.status_int).to.eq(302)
    expect(response.headers['Location']).to.eq('http://localhost/')

def test_register_when_user_exists_redirects_to_index(testbed, server):
    server.post('/auth/register', get_fixture())

    fixture = get_fixture().copy()
    fixture['passtest'] = 'blargh'
    response = server.post('/auth/register', fixture)

    expect(response.status).to.eq('302 Moved Temporarily')
    expect(response.status_int).to.eq(302)
    expect(response.headers['Location']).to.eq('http://localhost/')

def test_login_when_valid_form_starts_session(testbed, server):
    server.post('/auth/register', get_fixture())

    response = server.post('/auth/login', {
        'username': 'embar-test', 'password': 'somepass'
    })

    expect(response.status).to.eq('302 Moved Temporarily')
    expect(response.status_int).to.eq(302)
    expect(response.headers['Location']).to.eq('http://localhost/game/')

def test_login_when_invalid_form_returns_to_index(testbed, server):
    server.post('/auth/register', get_fixture())

    response = server.post('/auth/login', {
        'username': 'embar-test'
    })

    expect(response.status).to.eq('302 Moved Temporarily')
    expect(response.status_int).to.eq(302)
    expect(response.headers['Location']).to.eq('http://localhost/')

def test_login_when_credentials_invalid_returns_to_index(testbed, server):
    server.post('/auth/register', get_fixture())

    response = server.post('/auth/login', {
        'username': 'embar-test', 'password': 'bad-password'
    })

    expect(response.status).to.eq('302 Moved Temporarily')
    expect(response.status_int).to.eq(302)
    expect(response.headers['Location']).to.eq('http://localhost/')
