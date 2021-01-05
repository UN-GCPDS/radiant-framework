"""
Radiant

"""
import os
import sys
import random
import jinja2
from xml.etree import ElementTree

try:
    import browser
    sys.exit()
except:
    pass


import json

import importlib.util

from tornado.web import Application, url, RequestHandler, StaticFileHandler
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer


sys.path.append(os.path.join(os.path.dirname(__file__), 'fake_modules'))


RadiantAPI = object
DEBUG = True


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
class ThemeHandler(RequestHandler):

    # ----------------------------------------------------------------------
    def get(self):
        theme = self.get_theme()
        loader = jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates'))
        env = jinja2.Environment(autoescape=True, loader=loader)
        env.filters['vector'] = self.hex2vector
        stylesheet = env.get_template('theme.css.template')
        self.write(stylesheet.render(**theme))

    # ----------------------------------------------------------------------
    @staticmethod
    def hex2vector(hex_):
        """"""
        return ', '.join([str(int(hex_[i:i + 2], 16)) for i in range(1, 6, 2)])

    # ----------------------------------------------------------------------
    def get_theme(self):
        theme = self.settings['theme']

        if (not theme) or (not os.path.exists(theme)):
            theme = os.path.join(os.path.dirname(__file__), 'templates', 'default_theme.xml')

        tree = ElementTree.parse(theme)
        theme_css = {child.attrib['name']: child.text for child in tree.getroot()}
        return theme_css


########################################################################
class RadiantHandler(RequestHandler):
    def get(self):
        class_ = self.settings['class']
        python_ = self.settings['python']
        module = self.settings['module']
        file = self.settings['file']
        argv = json.dumps(self.settings['argv'])
        # port = self.settings['port']
        # seed = self.settings['seed']
        # mode = 'dashboard'

        variables = locals().copy()
        variables.pop('self')
        self.render("templates/index.html", **variables)


# ----------------------------------------------------------------------
def make_app(class_, python, websockethandler, theme):

    settings = {
        "debug": DEBUG,
        'static_path': os.path.join(os.path.dirname(__file__), 'brython'),
        'static_url_prefix': '/static/',
        "xsrf_cookies": False,
        'class': class_,
        'python': python if python else (None, None),
        'module': os.path.split(sys.path[0])[-1],
        'file': os.path.split(sys.argv[0])[-1].removesuffix('.py'),
        # 'autoreload': False,
        'theme': theme,
        'argv': sys.argv,
    }

    app = [
        url(r'^/$', RadiantHandler),
        url(r'^/theme.css$', ThemeHandler),
        url(r'^/root/(.*)', StaticFileHandler, {'path': sys.path[0]}),
    ]

    if python:
        spec = importlib.util.spec_from_file_location('.'.join(python).replace('.py', ''), os.path.abspath(python[0]))
        foo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(foo)
        app.append(url(r'^/python_handler', getattr(foo, python[1])))

    if websockethandler:
        spec = importlib.util.spec_from_file_location('.'.join(websockethandler).replace('.py', ''), os.path.abspath(websockethandler[0]))
        foo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(foo)
        app.append(url(r'^/ws', getattr(foo, websockethandler[1])))

    return Application(app, **settings)


# ----------------------------------------------------------------------
def RadiantServer(class_, host='localhost', port='5000', python=None, websockethandler=None, theme=None):
    """"""
    print("Radiant server running on port {}".format(port))
    application = make_app(class_, python, websockethandler, theme)
    http_server = HTTPServer(application)
    http_server.listen(port, host)
    IOLoop.instance().start()


