# Radiant
Brython framework

![GitHub top language](https://img.shields.io/github/languages/top/un-gcpds/radiant?)
![PyPI - License](https://img.shields.io/pypi/l/radiant?)
![PyPI](https://img.shields.io/pypi/v/radiant?)
![PyPI - Status](https://img.shields.io/pypi/status/radiant?)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/radiant?)
![GitHub last commit](https://img.shields.io/github/last-commit/un-gcpds/radiant?)
![CodeFactor Grade](https://img.shields.io/codefactor/grade/github/UN-GCPDS/radiant?)
[![Documentation Status](https://readthedocs.org/projects/radiant/badge/?version=latest)](https://radiant.readthedocs.io/en/latest/?badge=latest)



## Instalation


```python
pip install radiant
```

## Usage


```python
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
```
