#!brython

from radiant.server import RadiantAPI, pyscript, pyscript_globals, pyscript_init
from browser import document, html
import bootstrap as bs
import logging


########################################################################
class BareMinimum(RadiantAPI):

    # ----------------------------------------------------------------------
    def __init__(self, *args, **kwargs):
        """"""
        super().__init__(*args, **kwargs)
        document.select_one('body') <= html.H1('Radiant-Framework')

        document.select_one('body') <= bs.Button('Non-inline Arg', 'primary', on_click=lambda evt: self.plot_non_inline_arg(5))
        document.select_one('body') <= bs.Button('Non-inline', 'primary', on_click=lambda evt: self.plot_non_inline())
        document.select_one('body') <= bs.Button('Test callback', 'danger', on_click=lambda evt: self.test_callback())

        self.create_environ()
        # self.test_callback_inline()
        # self.plot_inline_arg(f=30)
        # self.plot_inline()

    # ----------------------------------------------------------------------
    def create_environ(self):
        """"""
        for i in range(4):
            document.select_one('body') <= html.DIV(id=f'mpl{i + 1}')

    # ----------------------------------------------------------------------
    @pyscript_globals
    def _(self):
        """"""
        import numpy as np
        from matplotlib import pyplot as plt
        import json

    # ----------------------------------------------------------------------
    @pyscript(output='mpl1', callback='callback')
    def plot_non_inline_arg(self, f):
        """"""
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.set_title('Non-inline function [ARG]')
        x = np.linspace(0, 10, 1000)
        y = np.sinc(2 * np.pi * f * x)
        ax.plot(x, y, color='C1')

        return fig

    # ----------------------------------------------------------------------
    @pyscript(output='mpl2', callback='callback')
    def plot_non_inline(self):
        """"""
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.set_title('Non-inline function')
        x = np.linspace(0, 10, 1000)
        y = np.sinc(2 * np.pi * 1 * x)
        ax.plot(x, y, color='C1')

        return fig

    # ----------------------------------------------------------------------
    # @pyscript(inline=True, output='mpl3', callback='callback')
    @pyscript(inline=True, output='mpl3')
    def plot_inline_arg(self, f):
        """"""
        import numpy as np
        from matplotlib import pyplot as plt

        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.set_title('Inline function [ARG]')
        x = np.linspace(0, 10, 1000)
        y = np.sin(2 * np.pi * f * x)
        ax.plot(x, y, color='C1')

        return fig

    # ----------------------------------------------------------------------
    @pyscript(inline=True)
    def plot_inline(self, output='mpl4'):
        """"""
        import numpy as np
        from matplotlib import pyplot as plt

        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.set_title('Inline function')
        x = np.linspace(0, 10, 1000)
        y = np.sin(2 * np.pi * 5 * x)
        ax.plot(x, y, color='C1')

        return fig

    # ----------------------------------------------------------------------
    @pyscript(inline=True, callback='callback')
    def test_callback_inline(self):
        """"""
        print('Callback inline')
        import json
        return json.dumps({'A': 100})

    # ----------------------------------------------------------------------

    @pyscript(callback='callback')
    def test_callback(self):
        """"""
        print('Callback not-inline')
        import json
        return json.dumps({'B': 100})

    # ----------------------------------------------------------------------
    def callback(self, *args, **kwargs):
        """"""
        print('Callback called')
        logging.warning('Callback:')
        logging.warning(f'#' * 20)
        logging.warning('CALLBACK')
        logging.warning(f'{args}, {kwargs}')

    # ----------------------------------------------------------------------
    @pyscript_init
    def asdf(self):
        """"""
        test_callback_inline()


if __name__ == '__main__':
    BareMinimum()
