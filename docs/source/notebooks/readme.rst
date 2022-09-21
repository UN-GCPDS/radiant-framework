Radiant Framework
=================

A Brython/PyScript Framework for Web Apps development.

|GitHub top language| |PyPI - License| |PyPI| |PyPI - Status| |PyPI -
Python Version| |GitHub last commit| |CodeFactor Grade| |Documentation
Status|

Radiant is a `Brython <https://brython.info/>`__ and
`PyScript <https://pyscript.net/>`__ framework for the quick development
of web apps using *Python* syntax, so there is no need to care about (if
you don’t want) HTML, CSS, or JavaScript. This is basically a set of
scripts that allows the same file run from *Python* and
*Brython*/*PyScript*, when is running under *Python* a
`Tornado <https://www.tornadoweb.org/>`__ server is created and
configure the local path for serving static files, at the same time a
custom HTML template is configured at runtime to import the same script,
this time under *Brython*/*PyScript*.

.. |GitHub top language| image:: https://img.shields.io/github/languages/top/un-gcpds/brython-radiant?
.. |PyPI - License| image:: https://img.shields.io/pypi/l/radiant?
.. |PyPI| image:: https://img.shields.io/pypi/v/radiant?
.. |PyPI - Status| image:: https://img.shields.io/pypi/status/radiant?
.. |PyPI - Python Version| image:: https://img.shields.io/pypi/pyversions/radiant?
.. |GitHub last commit| image:: https://img.shields.io/github/last-commit/un-gcpds/brython-radiant?
.. |CodeFactor Grade| image:: https://img.shields.io/codefactor/grade/github/UN-GCPDS/brython-radiant?
.. |Documentation Status| image:: https://readthedocs.org/projects/radiant/badge/?version=latest
   :target: https://radiant-framework.readthedocs.io/en/latest/?badge=latest

Instalation
-----------

.. code:: ipython3

    pip install radiant

Brython: bare minimum
---------------------

.. code:: ipython3

    #!bryhton
    
    from radiant.server import RadiantAPI
    from browser import document, html
    
    
    class BareMinimum(RadiantAPI):
    
        def __init__(self, *args, **kwargs):
            """"""
            super().__init__(*args, **kwargs)
            document.select_one('body') <= html.H1('Radiant-Framework')
    
    
    if __name__ == '__main__':
        BareMinimum()

PyScript: bare minimum
----------------------

This example use a ``requirements.txt`` file to install dependencies.

.. code:: ipython3

    #requirements.txt
    
    numpy
    matplotlib

.. code:: ipython3

    #!pyscript
    
    import numpy as np
    from matplotlib import pyplot as plt
    from radiant.server import RadiantAPI
    import js
    
    
    class BareMinimum(RadiantAPI):
    
        def __init__(self):
            print('Radiant-Framework')
            self.plot()
    
        def plot(self):
            """"""
            fig = plt.figure()
            ax = fig.add_subplot(111)
            x = np.linspace(0, 10, 1000)
            y = np.sin(x)
            ax.plot(x, y)
            js.document.body.prepend(self.fig2img(fig))
    
    
    if __name__ == '__main__':
        BareMinimum()

Brython + PyScript
------------------

.. code:: ipython3

    #!brython
    
    from radiant.server import RadiantAPI, pyscript
    from browser import document, html
    
    
    class BareMinimum(RadiantAPI):
    
        def __init__(self, *args, **kwargs):
            """"""
            super().__init__(*args, **kwargs)
            document.select_one('body') <= html.H1('Radiant-Framework')
    
            document.select_one('body') <= html.DIV(id='mpl')
            self.plot_sin(f=5)  # will render on #mpl every time
    
            document.select_one('body') <= self.plot_sinc(f=1)  
    
            
        # will render on #mpl every time
        @pyscript(output='mpl')
        def plot_sin(self, f=10):
            """"""
            import numpy as np
            from matplotlib import pyplot as plt
    
            fig = plt.figure()
            ax = fig.add_subplot(111)
            x = np.linspace(0, 1, 1000)
            y = np.sin(2 * np.pi * f * x)
            ax.plot(x, y)
    
            return fig
    
        
        # will return the image object
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
        BareMinimum()
