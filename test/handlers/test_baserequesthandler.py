from robber import expect
from webapp2 import WSGIApplication
from webtest import TestApp as WebTest
from app.handlers import BaseRequestHandler

class ExampleRequestHandler(BaseRequestHandler):
    def get(self, test):
        if test == 'json-object':
            return self.json_view({'test': test})
        if test == 'json-kwargs':
            return self.json_view(test=test)
        if test == 'json-object-first':
            return self.json_view({'test': test}, test='skipped')
        if test == 'html-template':
            return self.html_view('template.html', test=test)
        if test == 'session-start':
            self.session['test'] = self.request.get('key')
            return
        if test == 'session-read':
            return self.json_view(session=self.session.get('test'))
        if test == 'session-end':
            del self.session['test']
            return

app = WebTest(WSGIApplication([
    (r'/(.+)', ExampleRequestHandler)
], config={
    'webapp2_extras.sessions': {
        'secret_key': 'test-secret-session-key'
    },
    'template_path': 'test/html'
}))

def test_get_json_view_test_object():
    response = app.get('/json-object')

    expect(response.status).to.eq('200 OK')
    expect(response.status_int).to.eq(200)
    expect(response.content_type).to.eq('application/json')
    expect(response.content_length).to.be.above(0)
    expect(response.json).to.eq({u'test': u'json-object'})

def test_get_json_view_test_kwargs():
    response = app.get('/json-kwargs')

    expect(response.status).to.eq('200 OK')
    expect(response.status_int).to.eq(200)
    expect(response.content_type).to.eq('application/json')
    expect(response.content_length).to.be.above(0)
    expect(response.json).to.eq({u'test': u'json-kwargs'})

def test_get_json_view_test_object_overrides_kwargs():
    response = app.get('/json-object-first')

    expect(response.status).to.eq('200 OK')
    expect(response.status_int).to.eq(200)
    expect(response.content_type).to.eq('application/json')
    expect(response.content_length).to.be.above(0)
    expect(response.json).to.eq({u'test': u'json-object-first'})

def test_get_html_renders_template():
    response = app.get('/html-template')

    expect(response.status).to.eq('200 OK')
    expect(response.status_int).to.eq(200)
    expect(response.content_type).to.eq('text/html')
    expect(response.content_length).to.be.above(0)
    expect(response.text).to.eq('content: html-template')

def test_session_state_is_saveable_and_removeable():
    r1 = app.get('/session-start?key=foo')
    expect(r1.status).to.eq('200 OK')

    r2 = app.get('/session-read')
    expect(r2.json).to.eq({u'session': u'foo'})

    r3 = app.get('/session-end')
    expect(r3.status).to.eq('200 OK')

    r2 = app.get('/session-read')
    expect(r2.json).to.eq({u'session': None})
