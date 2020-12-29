import os
import sys
import random

import json

import importlib.util

from tornado.web import Application, url, RequestHandler, StaticFileHandler
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer


sys.path.append(os.path.join(os.path.dirname(__file__), 'fake_modules'))


RadiantAPI = object
DEBUG = True

if len(sys.argv) > 1:
    port = sys.argv[1]
else:
    port = '5000'


########################################################################
class PythonHandler(RequestHandler):
    def post(self):
        name = self.get_argument('name')
        args = tuple(json.loads(self.get_argument('args')))
        kwargs = json.loads(self.get_argument('kwargs'))

        if v := getattr(self, name, None)(*args, **kwargs):
            if v is None:
                data = json.dumps({'__RDNT__': 0, })
            else:
                data = json.dumps({'__RDNT__': v, })
        self.write(data)

    # ----------------------------------------------------------------------
    def test(self):
        """"""
        return True


########################################################################
class RadiantHandler(RequestHandler):
    def get(self):
        class_ = self.settings['class']
        python_ = self.settings['python']
        module = self.settings['module']
        file = self.settings['file']
        port = self.settings['port']
        seed = self.settings['seed']
        mode = 'dashboard'

        variables = locals().copy()
        variables.pop('self')
        self.render("templates/index.html", **variables)


# ----------------------------------------------------------------------
def make_app(class_, python):

    settings = {
        "debug": DEBUG,
        'static_path': os.path.join(os.path.dirname(__file__), 'brython'),
        'static_url_prefix': '/static/',
        "xsrf_cookies": False,
        'class': class_,
        'python': python if python else (None, None),
        'module': os.path.split(sys.path[0])[-1],
        'file': os.path.split(sys.argv[0])[-1].removesuffix('.py'),
        'port': port,
        'autoreload': False,
        'seed': random.randint(0, 1000),
    }

    app = [
        url(r'^/$', RadiantHandler),
        url(r'^/root/(.*)', StaticFileHandler, {'path': sys.path[0]}),
        # url(r'^/python_handler', PythonHandler),
        # url(r'^/ws', WSHandler),
    ]

    if python:
        spec = importlib.util.spec_from_file_location('.'.join(python).replace('.py', ''), os.path.abspath(python[0]))
        foo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(foo)
        app.append(url(r'^/python_handler', getattr(foo, python[1])))

    return Application(app, **settings)


# ----------------------------------------------------------------------
def RadiantServer(class_, python=None):
    """"""
    print("Radiant server running on port {}".format(port))
    application = make_app(class_, python)
    http_server = HTTPServer(application)
    http_server.listen(port, '0.0.0.0')
    IOLoop.instance().start()


