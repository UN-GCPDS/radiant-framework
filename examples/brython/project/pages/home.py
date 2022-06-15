from radiant.server import RadiantAPI
from browser import document, html
import logging

########################################################################
class Home(RadiantAPI):

    # ----------------------------------------------------------------------
    def __init__(self, *args, **kwargs):
        """"""
        super().__init__(*args, **kwargs)
        document.select_one('body') <= html.H1('Hello World')

        document.select_one('body') <= html.H1('Multipage support')
        document.select_one('body') <= html.A(
            'second page', href='/multipage')

        logging.warning('HOLA')


