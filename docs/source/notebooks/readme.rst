Brython-Radiant
===============

A Brython Framework for Web Apps development.

|GitHub top language| |PyPI - License| |PyPI| |PyPI - Status| |PyPI -
Python Version| |GitHub last commit| |CodeFactor Grade| |Documentation
Status|

Radiant is a `Brython <https://brython.info/>`__ framework for the quick
development of web apps with pure Python/Brython syntax so there is no
need to care about (if you don’t want) HTML, CSS, or Javascript. Run
over `Tornado <https://www.tornadoweb.org/>`__ servers and include
support to
`Websockets <notebooks/02-additional_features.ipynb#WebSockets>`__,
`Python
Scripts <notebooks/02-additional_features.ipynb#Python-scripting>`__ and
`MDC <notebooks/02-additional_features.ipynb#Custom-themes>`__.

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

Usage
-----

Bare minimum
~~~~~~~~~~~~

.. code:: ipython3

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

Extra options
~~~~~~~~~~~~~

.. code:: ipython3

    # Radiant modules
    from radiant.server import RadiantAPI, RadiantServer  # import RadiantServer for advanced options
    
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

How to works
------------

This is basically a set of scripts that allows the same file run from
*Python* and *Brython*, when is running under *Python* a
`Tornado <https://www.tornadoweb.org/>`__ server is created and
configure the local path for serving static files, and a custom HTML
template is configured in runtime to import the same script, this time
under *Brython*, is very simple.
