"""
Radiant

"""
# Prevent this file to be imported from Brython
import sys
try:
    import browser
    sys.exit()
except:
    pass

import os
import json
import jinja2
import pathlib
import importlib.util
from xml.etree import ElementTree
from typing import Union, List, Tuple, Optional

from tornado.web import Application, url, RequestHandler, StaticFileHandler
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer

DEBUG = True
PATH = Union[str, pathlib.Path]
URL = str
DEFAULT_IP = 'localhost'
DEFAULT_PORT = '5000'
DEFAULT_BRYTHON_VERSION = '3.10.3'
DEFAULT_BRYTHON_DEBUG = 0


########################################################################
class RadiantAPI:
    """Rename Randiant with a new class."""

    # ---------------------------------------------------------------------
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # ----------------------------------------------------------------------
    def __new__(self):
        """"""
        RadiantServer(self.__name__)


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
        loader = jinja2.FileSystemLoader(os.path.join(
            os.path.dirname(__file__), 'templates'))
        env = jinja2.Environment(autoescape=True, loader=loader)
        env.filters['vector'] = self.hex2vector
        stylesheet = env.get_template('theme.css.template')
        self.write(stylesheet.render(**theme))

    # ----------------------------------------------------------------------
    @staticmethod
    def hex2vector(hex_: str):
        return ', '.join([str(int(hex_[i:i + 2], 16)) for i in range(1, 6, 2)])

    # ----------------------------------------------------------------------
    def get_theme(self):
        theme = self.settings['theme']

        if (not theme) or (not os.path.exists(theme)):
            theme = os.path.join(os.path.dirname(__file__),
                                 'templates', 'default_theme.xml')

        tree = ElementTree.parse(theme)
        theme_css = {child.attrib['name']
            : child.text for child in tree.getroot()}
        return theme_css


# ########################################################################
# class ManifestHandler(RequestHandler):

    # # ----------------------------------------------------------------------
    # def get(self):

        # with open('/home/yeison/Development/BCI-Framework/brython-radiant/examples/pwa/manifest.json', 'r') as file:
            # content = file.read()

        # self.write(content)


########################################################################
class RadiantHandler(RequestHandler):

    def initialize(self, **kwargs):
        self.initial_arguments = kwargs

    def get(self):
        variables = self.settings.copy()
        variables.update(self.initial_arguments)

        variables['argv'] = json.dumps(variables['argv'])
        self.render(
            f"{os.path.realpath(variables['template'])}", **variables)


# ----------------------------------------------------------------------
def make_app(class_: str, /,
             brython_version: str,
             debug_level: int,
             pages: Tuple[str],
             template: PATH = os.path.join(os.path.dirname(
                 __file__), 'templates', 'index.html'),
             environ: dict = {},
             mock_imports: Tuple[str] = [],
             handlers: Tuple[URL, Union[List[Union[PATH, str]],
                                        RequestHandler], dict] = (),
             python: Tuple[PATH, str] = (),
             theme: PATH = None,
             path: PATH = None,
             autoreload: bool = False,
             ):
    """
    Parameters
    ----------
    class_ :
        The main class name as string.
    template :
        Path for HTML file with the template.
    environ :
        Dictionary with arguments accessible from the template and main class.
    mock_imports :
        List with modules that exist in Python but not in Brython, this prevents
        imports exceptions.
    handlers :
        Custom handlers for server.
    python :
        Real Python scripting handler.
    theme :
        Path for the XML file with theme colors.
    path :
        Custom directory accesible from Brython PATH.
    autoreload :
        Activate the `autoreload` Tornado feature.
    """

    settings = {
        "debug": DEBUG,
        'static_path': os.path.join(os.path.dirname(__file__), 'static'),
        'static_url_prefix': '/static/',
        "xsrf_cookies": False,
        'autoreload': autoreload,
    }

    environ.update({
        'class_': class_,
        'python_': python if python else (None, None),
        'module': os.path.split(sys.path[0])[-1],
        'file': os.path.split(sys.argv[0])[-1].replace('.py', ''),
        # 'file': os.path.split(sys.argv[0])[-1].removesuffix('.py'),
        'theme': theme,
        'argv': sys.argv,
        'template': template,
        'mock_imports': mock_imports,
        'path': path,
        'brython_version': brython_version,
        'debug_level': debug_level,
    })

    app = []
    if class_:
        app += [url(r'^/$', RadiantHandler, environ)]

    app += [
        url(r'^/theme.css$', ThemeHandler),
        url(r'^/root/(.*)', StaticFileHandler, {'path': sys.path[0]}),
        # url(r'^/manifest.json$', ManifestHandler),
    ]

    if isinstance(pages, str):
        *package, module_name = pages.split('.')
        module = importlib.import_module('.'.join(package))
        pages = getattr(module, module_name)

    for url_, module in pages:
        *file_, class_ = module.split('.')
        environ_tmp = environ.copy()
        file_ = '.'.join(file_)
        environ_tmp['file'] = file_
        environ_tmp['class_'] = class_
        app.append(url(url_, RadiantHandler, environ_tmp),)

    if python:
        spec = importlib.util.spec_from_file_location(
            '.'.join(python).replace('.py', ''), os.path.abspath(python[0]))
        foo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(foo)
        app.append(url(r'^/python_handler', getattr(foo, python[1])))

    for handler in handlers:
        if isinstance(handler[1], tuple):
            spec = importlib.util.spec_from_file_location(
                '.'.join(handler[1]).replace('.py', ''), os.path.abspath(handler[1][0]))
            foo = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(foo)
            app.append(url(handler[0], getattr(
                foo, handler[1][1]), handler[2]))
        else:
            app.append(url(*handler))

    if path:
        app.append(url(r'^/path/(.*)', StaticFileHandler, {'path': path}),)

    settings.update(environ)

    return Application(app, **settings)


# ----------------------------------------------------------------------
def RadiantServer(class_: Optional[str] = None,
                  host: str = DEFAULT_IP,
                  port: str = DEFAULT_PORT,
                  pages: Tuple[str] = (),
                  brython_version: str = DEFAULT_BRYTHON_VERSION,
                  debug_level: int = DEFAULT_BRYTHON_DEBUG,
                  template: PATH = os.path.join(os.path.dirname(
                      __file__), 'templates', 'index.html'),
                  environ: dict = {},
                  mock_imports: Tuple[str] = [],
                  handlers: Tuple[URL, Union[List[Union[PATH, str]],
                                             RequestHandler], dict] = (),
                  python: Tuple[PATH, str] = (),
                  theme: Optional[PATH] = None,
                  path: Optional[PATH] = None,
                  autoreload: Optional[bool] = False,
                  callbacks: Optional[tuple] = (),
                  **kwargs,
                  ):
    """Python implementation for move `class_` into a Bython environment.

    Configure the Tornado server and the Brython environment for run the
    `class_` in both frameworks at the same time.

    Parameters
    ----------
    class_ :
        The main class name as string.
    host :
        The host for server.
    port :
        The port for server.
    template :
        Path for HTML file with the template.
    environ :
        Dictionary with arguments accessible from the template and main class.
    mock_imports :
        List with modules that exist in Python but not in Brython, this prevents
        imports exceptions.
    handlers :
        Custom handlers for server.
    python :
        Real Python scripting handler.
    theme :
        Path for the XML file with theme colors.
    path :
        Custom directory accesible from Brython PATH.
    autoreload :
        Activate the `autoreload` Tornado feature.

    """

    print("Radiant server running on port {}".format(port))
    application = make_app(class_, python=python, template=template,
                           handlers=handlers, theme=theme, environ=environ,
                           mock_imports=mock_imports, path=path,
                           brython_version=brython_version, pages=pages,
                           debug_level=debug_level)
    http_server = HTTPServer(application,
                             # ssl_options={
                             # 'certfile': 'host.crt',
                             # 'keyfile': 'host.key',
                             # },
                             )
    http_server.listen(port, host)

    for handler in callbacks:
        if isinstance(handler, tuple):
            spec = importlib.util.spec_from_file_location(
                '.'.join(handler).replace('.py', ''), os.path.abspath(handler[0]))
            foo = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(foo)
            getattr(foo, handler[1])()
            # app.append(url(handler[0], getattr(foo, handler[1][1]), handler[2]))
        else:
            handler()

    IOLoop.instance().start()


