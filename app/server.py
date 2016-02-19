import os, logging
from webapp2 import Route, WSGIApplication
from .handlers import *

config = {
    'template_path': 'app/html',
    'webapp2_extras.sessions': {
        'secret_key': os.environ['EMBAR_SESSION']
    }
}

wsgi = WSGIApplication([
    Route('/', handler=PublicRequestHandler, handler_method='get_index')
], debug=True, config=config)
