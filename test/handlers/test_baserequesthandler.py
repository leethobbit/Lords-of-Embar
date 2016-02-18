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

app = WebTest(WSGIApplication([
    (r'/(.+)', ExampleRequestHandler)
]))

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
