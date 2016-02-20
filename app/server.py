from __future__ import unicode_literals
import os, logging
from webapp2 import Route, WSGIApplication
from .handlers import *

config = {
    'template_path': 'app/html',
    'webapp2_extras.sessions': {
        'secret_key': os.environ['EMBAR_SESSION'].encode()
    }
}

wsgi = WSGIApplication([
    # PublicRequestHandler
    Route('/',
        handler=PublicRequestHandler, handler_method='get_index'),

    # AuthRequestHandler
    Route('/auth/register',
        handler=AuthRequestHandler, handler_method='post_register'),
    Route('/auth/login',
        handler=AuthRequestHandler, handler_method='post_login'),
    Route('/auth/logout',
        handler=AuthRequestHandler, handler_method='get_logout')

], debug=True, config=config)
