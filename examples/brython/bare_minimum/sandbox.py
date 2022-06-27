#!bryhton

from radiant.server import RadiantAPI
from browser import document, html
import logging
from mdc.MDCTab import MDCTabBar


########################################################################
class BareMinimum(RadiantAPI):

    # ----------------------------------------------------------------------
    def __init__(self, *args, **kwargs):
        """"""
        super().__init__(*args, **kwargs)
        document.select_one('body') <= html.H1('Hello World')

        # <i class = "fa-solid fa-right" > < / i >

        document.select_one('body') <= html.I(Class='fas fa-arrow-right')

        logging.warning('HOLA')

        tabbar = MDCTabBar(
            {'text': 'Python', 'id': 'python'},
            {'text': 'Pinguino', 'id': 'pinguino'},
        )

        document.select_one('body') <= tabbar
        document.select_one('body') <= tabbar.panels

        tabbar.panel['python'] <= html.SPAN('PYTHON')
        tabbar.panel['pinguino'] <= html.SPAN('PINGUINO')


if __name__ == '__main__':
    BareMinimum()
