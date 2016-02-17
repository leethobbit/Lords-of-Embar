from __future__ import unicode_literals
import os, sys

# Testing Modules
import pytest
import httpretty
from webtest import TestApp

# set appengine on path
sdk_path = '/usr/local/bin'
sys.path.insert(0, sdk_path)
sys.path.insert(1, os.path.join(os.getcwd(), '.'))

import dev_appserver
dev_appserver.fix_sys_path()

try:
    import appengine_config
    (appengine_config)
except ImportError:
    print '[LOG] unable to import appengine_config'

# Google App Engine modules
from google.appengine.ext import ndb
from google.appengine.ext import testbed as _testbed

# application fixtures
@pytest.fixture(scope='module')
def server():
    import app.server
    return TestApp(app.server.wsgi)

# requests fixtures
@pytest.fixture
def http_mock(request):
    httpretty.enable()
    request.addfinalizer(httpretty.disable)
    return httpretty

# datastore fixtures
@pytest.fixture
def testbed(request):
    bed = _testbed.Testbed()
    bed.activate()
    bed.init_datastore_v3_stub()
    bed.init_memcache_stub()
    ndb.get_context().clear_cache()
    request.addfinalizer(bed.deactivate)
    return bed
