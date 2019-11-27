import sys

path = '/var/www/tagger.gogyup.net'
if path not in sys.path:
    sys.path.append(path)

from tagger import __hug_wsgi__ as application
