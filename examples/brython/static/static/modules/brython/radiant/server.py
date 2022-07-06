import os

from browser import html, document
from .utils import LocalInterpreter
import inspect
from string import ascii_lowercase
import random
import logging

RadiantServer = None
PYSCRIPT = html.maketag('py-script')


# ----------------------------------------------------------------------
def pyscript(output=None):
    """"""
    if callable(output):
        logging.error(f'ERROR: {output.__name__}')
        logging.error(f'Decorator must be instantiated: @pyscript()')
        logging.error(f'                                         ^^')

    # ----------------------------------------------------------------------
    def wrapargs(fn):

        def wrap(*args, **kwargs):

            # Output
            if output is None:
                output_id = 'pyscript-' + \
                    ''.join([random.choice(ascii_lowercase)
                            for _ in range(16)])
                out = html.DIV(id=output_id)
                document.select_one('body') <= out
            else:
                output_id = output

            # Source code
            source = inspect.getsource(fn)
            logging.warning(f'*{args[1:]}, **{kwargs}')
            source += f'{fn.__name__}(None, *{args[1:]}, **{kwargs})'

            # Input
            py_script = PYSCRIPT(source)
            py_script.attrs['output'] = output_id
            document.select_one('body') <= py_script

            if output is None:
                return out

        return wrap
    return wrapargs


########################################################################
class RadiantAPI:
    """"""

    # ----------------------------------------------------------------------
    def __init__(self, class_, python=None, **kwargs):
        """"""
        if python[0] and python[0] != 'None':
            setattr(self, python[1], LocalInterpreter())

    # ----------------------------------------------------------------------
    def add_css_file(self, file):
        """"""
        document.select('head')[0] <= html.LINK(
            href=os.path.join('root', file), type='text/css', rel='stylesheet')
