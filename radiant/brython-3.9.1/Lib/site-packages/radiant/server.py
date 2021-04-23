import os

from browser import html, document
from .utils import LocalInterpreter

RadiantServer = None


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
