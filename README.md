# Lords of Embar

## Installation

```
$ git clone <repository-url>
$ cd lords-of-embar
$ /path/to/dev_appserver.py .
```

## Unit Tests

Virtual Environment and requirements.txt are only required for running
the tests. The development server should handle any App Engine dependencies.

```
$ virtualenv -p `which python2` venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ py.test -rw
```
