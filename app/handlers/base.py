from webapp2 import RequestHandler
from webapp2_extras import json


class BaseRequestHandler(RequestHandler):
    def json_view(self, content=None, **kwds):
        content = content or kwds
        self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
        self.response.write(json.encode(content))
