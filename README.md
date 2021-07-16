# Brython-Radiant

A Brython Framework for Web Apps development.

![GitHub top language](https://img.shields.io/github/languages/top/un-gcpds/brython-radiant?)
![PyPI - License](https://img.shields.io/pypi/l/radiant?)
![PyPI](https://img.shields.io/pypi/v/radiant?)
![PyPI - Status](https://img.shields.io/pypi/status/radiant?)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/radiant?)
![GitHub last commit](https://img.shields.io/github/last-commit/un-gcpds/brython-radiant?)
![CodeFactor Grade](https://img.shields.io/codefactor/grade/github/UN-GCPDS/brython-radiant?)
[![Documentation Status](https://readthedocs.org/projects/radiant/badge/?version=latest)](https://radiant-framework.readthedocs.io/en/latest/?badge=latest)

Radiant is a [Brython](https://brython.info/) framework for the quick development of web apps wuth pure Python/Brython syntax which means that there is no need to care about (if you don't want) HTML, CSS, or Javascript.  Run over [Tornado](https://www.tornadoweb.org/) servers and includes support to [Websockets](notebooks/02-additional_features.ipynb#WebSockets), [Python Scripts](notebooks/02-additional_features.ipynb#Python-scripting) and [MDC](notebooks/02-additional_features.ipynb#Custom-themes).

## Instalation


```python
pip install radiant
```

## Usage


```python
# Radiant modules
from radiant.server import RadiantAPI

# Brython modules
from browser import document, html  # This modules are faked after `radiant` inport

# Main class inheriting RadiantAPI
class BareMinimum(RadiantAPI):

    # Constructor 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
        #-----------------------------------------------------------
        # Brython code (finally)
        document.select_one('body') <= html.H1('Hello World')
        #
        # ...all your brython code
        #-----------------------------------------------------------

# Run server
if __name__ == '__main__':
    BareMinimum()
```


```python
# Radiant modules
from radiant.server import RadiantAPI, RadiantServer  # import RadiantServer for advance options

from browser import document, html

# Main class inheriting RadiantAPI
class BareMinimum(RadiantAPI):

    def __init__(self, *args, **kwargs):
        """"""
        super().__init__(*args, **kwargs)

        #-----------------------------------------------------------
        # Brython code
        document.select_one('body') <= html.H1('Hello World')
        #
        # ...all your brython code
        #-----------------------------------------------------------
        
if __name__ == '__main__':
    # Advance options
    RadiantServer('BareMinimum',
                  host='localhost',
                  port=5000,
                  brython_version='3.9.1',
                  debug_level=0,
                  )
```

## How to works

This is basically a set of scripts that allows the same file run from _Python_ and _Brython_, when is running under _Python_ a [Tornado](https://www.tornadoweb.org/) server is created and configure the local path for serving static files, and a custom HTML template is configured in runtime to import the same script, this time under _Brython_, is very simple.
