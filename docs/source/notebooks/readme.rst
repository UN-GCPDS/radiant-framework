Radiant
=======

A Brython Framework for Web Apps development.

|GitHub top language| |PyPI - License| |PyPI| |PyPI - Status| |PyPI -
Python Version| |GitHub last commit| |CodeFactor Grade| |Documentation
Status|

Radiant is a `Brython <https://brython.info/>`__ framework for the quick
development of web apps from pure Python syntax which means that there
is no need to care about (if you don’t want) HTML, CSS, or Javascript.
It’s based on `Tornado <https://www.tornadoweb.org/>`__ servers and
includes support to
`Websockets <notebooks/10-advance_usage.html#WebSockets>`__, `Python
Scripts <notebooks/10-advance_usage.html#Python-scripting>`__ and
`MDC <notebooks/99-mdc.html>`__.

.. |GitHub top language| image:: https://img.shields.io/github/languages/top/un-gcpds/radiant?
.. |PyPI - License| image:: https://img.shields.io/pypi/l/radiant?
.. |PyPI| image:: https://img.shields.io/pypi/v/radiant?
.. |PyPI - Status| image:: https://img.shields.io/pypi/status/radiant?
.. |PyPI - Python Version| image:: https://img.shields.io/pypi/pyversions/radiant?
.. |GitHub last commit| image:: https://img.shields.io/github/last-commit/un-gcpds/radiant?
.. |CodeFactor Grade| image:: https://img.shields.io/codefactor/grade/github/UN-GCPDS/radiant?
.. |Documentation Status| image:: https://readthedocs.org/projects/radiant/badge/?version=latest
   :target: https://radiant-framework.readthedocs.io/en/latest/?badge=latest

Instalation
-----------

.. code:: ipython3

    pip install radiant

Usage
-----

.. code:: ipython3

    # Brython modules
    from browser import document, html
    
    # Radiant modules
    from radiant.server import RadiantAPI, RadiantServer
    
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
    
    # Execute server
    if __name__ == '__main__':
        RadiantServer('BareMinimum')

How to works
------------

This is basically a set of scripts that allows the same file run from
*Python* and *Brython*, when is running under *Python* a
`Tornado <https://www.tornadoweb.org/>`__ server is created and
configure the local path for serving static files, a custom HTML
template is configured in runtime to import the same script, this time
under *Brython*, is very simple.
