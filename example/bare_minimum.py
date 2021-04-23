from radiant.server import RadiantAPI
from browser import document, html
import logging

########################################################################
class BareMinimum(RadiantAPI):

    # ----------------------------------------------------------------------
    def __init__(self, *args, **kwargs):
        """"""
        super().__init__(*args, **kwargs)
        document.select_one('body') <= html.H1('Hello World')

        logging.warning('HOLA')


if __name__ == '__main__':
    BareMinimum()


