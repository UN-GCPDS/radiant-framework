import os

from browser import html, document, timer
from .utils import LocalInterpreter
import inspect
from string import ascii_lowercase
import random
import logging
import json

RadiantServer = None
PYSCRIPT = html.maketag('py-script')
# PYSCRIPTDEBUG = html.maketag('py-script-debug')
PYSCRIPTDEBUG = html.maketag('code')

PYSCRIPT_FUNTIONS = []


# ----------------------------------------------------------------------
def pyscript(output=None, inline=False, plotly_out=None, callback=None):
    """"""
    if callable(output):
        logging.error(f'ERROR: {output.__name__}')
        logging.error(f'Decorator must be instantiated: @pyscript()')
        logging.error(f'                                         ^^')

    # ----------------------------------------------------------------------
    def wrapargs(fn):

        def wrap(*args, **kwargs):

            # Output
            if (output is None or output == 'RAW') and (plotly_out is None):
                output_id = 'pyscript-' + \
                    ''.join([random.choice(ascii_lowercase)
                            for _ in range(16)])
                out = html.DIV(id=output_id)
                document.select_one('body') <= out
            else:
                if plotly_out is None:
                    output_id = output
                elif output is None:
                    output_id = plotly_out

            source = inspect.getsource(fn)
            if inline:
                # Source code
                if not fn.__name__ in PYSCRIPT_FUNTIONS:
                    PYSCRIPT_FUNTIONS.append(fn.__name__)
                    remove_after = False
                else:
                    source = f'# Function {fn.__name__} already defined\n'
                    remove_after = True
            else:
                source = ''
                remove_after = True

            if plotly_out:
                if inline:
                    source += f'\n\nrender_plotly_fig__({fn.__name__}(None, *{args[1:]}, **{kwargs}), "{output_id}")'
                else:
                    source += f'\n\nrender_plotly_fig__({fn.__name__}(*{args[1:]}, **{kwargs}), "{output_id}")'

            else:
                if inline:
                    source += f'\n\n{fn.__name__}(None, *{args[1:]}, **{kwargs})'
                else:
                    source += f'\n\n{fn.__name__}(*{args[1:]}, **{kwargs})'

            # document.select_one('body') <= PYSCRIPTDEBUG(source)
            py_script = PYSCRIPT(source)
            if inline:
                py_script.attrs['output'] = output_id
            document.select_one('body') <= py_script

            py_script.evaluate()
            if remove_after:
                # py_script.remove()
                py_script.style = {'display': 'none', }

            if (output is None) and (plotly_out is None):
                return out
            elif output is 'RAW':
                # on_callback(py_script, args[0])
                on_callback(py_script, args[0])
                return None

        return wrap
    return wrapargs


P = 0


def on_callback(element, fn):
    """"""
    global P

    P += 1
    if element.text or P > 200:
        print('calling...')
        fn.callback_fn(element.text)
        P = 0
    else:
        print(f'waiting... {element.text}')
        timer.set_timeout(lambda: on_callback(element, fn), 10)


########################################################################
class PyScriptAPI:
    """"""


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
