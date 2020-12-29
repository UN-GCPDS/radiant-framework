Radiant
=======

Brython framework

|GitHub top language| |PyPI - License| |PyPI| |PyPI - Status| |PyPI -
Python Version| |GitHub last commit| |CodeFactor Grade| |Documentation
Status|

.. |GitHub top language| image:: https://img.shields.io/github/languages/top/un-gcpds/radiant?
.. |PyPI - License| image:: https://img.shields.io/pypi/l/radiant?
.. |PyPI| image:: https://img.shields.io/pypi/v/radiant?
.. |PyPI - Status| image:: https://img.shields.io/pypi/status/radiant?
.. |PyPI - Python Version| image:: https://img.shields.io/pypi/pyversions/radiant?
.. |GitHub last commit| image:: https://img.shields.io/github/last-commit/un-gcpds/radiant?
.. |CodeFactor Grade| image:: https://img.shields.io/codefactor/grade/github/UN-GCPDS/radiant?
.. |Documentation Status| image:: https://readthedocs.org/projects/radiant/badge/?version=latest
   :target: https://radiant.readthedocs.io/en/latest/?badge=latest

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
    from radiant import RadiantAPI, RadiantServer
    
    
    # Main class inheriting RadiantAPI
    class BareMinimum(RadiantAPI):
    
        # Constructor 
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
        
            # Brython code (finally)
            document.select_one('body') <= html.H1('Hello World')
    
    # Execute server
    if __name__ == '__main__':
        RadiantServer('BareMinimum')
