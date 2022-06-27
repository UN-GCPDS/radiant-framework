# Radiant Framework

A Brython/PyScript Framework for Web Apps development.

![GitHub top language](https://img.shields.io/github/languages/top/un-gcpds/brython-radiant?)
![PyPI - License](https://img.shields.io/pypi/l/radiant?)
![PyPI](https://img.shields.io/pypi/v/radiant?)
![PyPI - Status](https://img.shields.io/pypi/status/radiant?)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/radiant?)
![GitHub last commit](https://img.shields.io/github/last-commit/un-gcpds/brython-radiant?)
![CodeFactor Grade](https://img.shields.io/codefactor/grade/github/UN-GCPDS/brython-radiant?)
[![Documentation Status](https://readthedocs.org/projects/radiant/badge/?version=latest)](https://radiant-framework.readthedocs.io/en/latest/?badge=latest)

Radiant is a [Brython](https://brython.info/) and [PyScript](https://pyscript.net/) framework for the quick development of web apps using _Python_ syntax, so there is no need to care about (if you don’t want) HTML, CSS, or Javascript. This is basically a set of scripts that allows the same file run from _Python_ and _Brython_/_PyScript_, when is running under _Python_ a [Tornado](https://www.tornadoweb.org/) server is created and configure the local path for serving static files, at the same time a custom HTML template is configured at runtime to import the same script, this time under _Brython_/_PyScript_.

## Instalation


```python
pip install radiant
```

## Brython: bare minimum


```python
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
```

## PyScript: bare minimum

This example use ```requirements.txt``` to install dependencies.


```python
#requirements.txt

numpy
matplotlib
```


```python
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
```

## Brython + PyScript


```python
#!brython

from radiant.server import RadiantAPI, pyscript
from browser import document, html


class BareMinimum(RadiantAPI):

    def __init__(self, *args, **kwargs):
        """"""
        super().__init__(*args, **kwargs)
        document.select_one('body') <= html.H1('Radiant-Framework')

        document.select_one('body') <= html.DIV(id='mpl')
        self.plot_sin(f=5)

        document.select_one('body') <= self.plot_sinc(f=1)

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
```
