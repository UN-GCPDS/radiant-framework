#!brython

from radiant.server import RadiantAPI, RadiantServer, pyscript
from browser import document, html
import logging


########################################################################
class BareMinimum(RadiantAPI):

    # ----------------------------------------------------------------------
    def __init__(self, *args, **kwargs):
        """"""
        super().__init__(*args, **kwargs)
        document.select_one('body') <= html.H1('Hello World')

        document.select_one('body') <= html.DIV(id='mpl')
        self.plot(f=1)

        document.select_one('body') <= self.plot_sinc(f=1)
        document.select_one('body') <= self.plot_sinc(f=2)
        document.select_one('body') <= self.plot_sinc(f=4)
        document.select_one('body') <= self.plot_sinc(f=8)

    # ----------------------------------------------------------------------
    @pyscript(output='mpl')
    def plot(self, f=10):
        """"""
        import numpy as np
        from matplotlib import pyplot as plt

        fig = plt.figure()
        ax = fig.add_subplot(111)
        x = np.linspace(0, 1, 1000)
        y = np.sin(2 * np.pi * f * x)
        ax.plot(x, y)

        return fig

    # ----------------------------------------------------------------------
    @pyscript()
    def plot_sinc(self, f):
        """"""
        import numpy as np
        from matplotlib import pyplot as plt

        fig = plt.figure()
        ax = fig.add_subplot(111)
        x = np.linspace(0, 10, 1000)
        y = np.sin(2 * np.pi * f * x)
        ax.plot(x, y, color='C1')

        return fig


if __name__ == '__main__':
    RadiantServer(
        'BareMinimum',
        pyscript=True,
    )
