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
def pyscript(output=None, inline=False, plotly_out=None, callback=None, id=None):
    """"""
    if callable(output):
        logging.error(f'ERROR: {output.__name__}')
        logging.error(f'Decorator must be instantiated: @pyscript()')
        logging.error(f'                                         ^^')

    # ----------------------------------------------------------------------
    def wrapargs(fn):

        def wrap(*args, **kwargs):

            # Output
            if (output is None) and (plotly_out is None):
                if id is None:
                    output_id = 'pyscript-' + \
                        ''.join([random.choice(ascii_lowercase)
                                for _ in range(16)])
                else:
                    output_id = id
                out = html.DIV(id=output_id)
                document.select_one('body') <= out
            else:
                if plotly_out is None:
                    output_id = output
                elif output is None:
                    output_id = plotly_out

            source = inspect.getsource(fn)
            remove_after = False
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
                # remove_after = True

            if plotly_out:
                if inline:
                    source += f'\n\nrender_plotly_fig__({fn.__name__}(None, *{args[1:]}, **{kwargs}), "{output_id}")'
                else:
                    source += f'\n\nrender_plotly_fig__({fn.__name__}(*{args[1:]}, **{kwargs}), "{output_id}")'

            else:
                if inline:
                    if args[1:]:
                        source += f'\n\n{fn.__name__}(None, *{args[1:]}, **{kwargs})'
                    else:
                        source += f'\n\n{fn.__name__}(None, **{kwargs})'
                else:
                    if args[1:]:
                        source += f'\n\n{fn.__name__}(*{args[1:]}, **{kwargs})'
                    else:
                        source += f'\n\n{fn.__name__}(**{kwargs})'

            # document.select_one('body') <= PYSCRIPTDEBUG(source)
            py_script = PYSCRIPT(source)
            if inline:
                py_script.attrs['output'] = output_id

            document.select_one('body') <= py_script
            py_script.evaluate()

            if remove_after or inline:
                print('%' * 70)
                print('%%%%Hidding py_script')
                py_script.style = {'display': 'none', }
                py_script.class_name += ' RADIANT-HIDE'

            if (output is None) and (plotly_out is None):
                print('%' * 70)
                print(f'%%%%Hidding out: {output_id}')
                document.select_one(f'#{output_id}').style = {'display': 'none', }
                out.style = {'display': 'none', }
                out.class_name += ' RADIANT-HIDE'
                py_script.style = {'display': 'none', }
                py_script.class_name += ' RADIANT-HIDE'

            if (output is None) and (plotly_out is None) and (not callback):
                return out
            # elif output is 'RAW':
            if callback:
                on_callback(py_script, args[0], callback, out)
                return None

        return wrap
    return wrapargs


# ----------------------------------------------------------------------
def pyscript_globals(fn):
    """"""
    return None


P = 0


def on_callback(element, fn, callback, out):
    """"""
    global P

    if ':' in callback:
        n = int(callback[callback.find(':') + 1:])
        callback = callback[:callback.find(':')]
    else:
        n = 100

    P += 1
    if element.text or P > n:
        print(f'Xxcalling...')
        print(f'Xx{element.text}xX')
        print(f'Xx{out.text}xX')
        try:
            getattr(fn, callback)(json.loads(element.text))
        except:
            getattr(fn, callback)(json.loads(out.text))
        P = 0
    else:
        print(f'waiting... {element.text}')
        timer.set_timeout(lambda: on_callback(element, fn, callback, out), 10)


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

    # # ----------------------------------------------------------------------
    # def on_load(self, callback, evt='DOMContentLoaded'):
        # """"""
        # logging.warning('#' * 30)
        # logging.warning('#' * 30)
        # document.addEventListener('load', callback)
        # logging.warning('#' * 30)
        # logging.warning('#' * 30)

