from radiant.server import RadiantAPI, RadiantServer
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
    RadiantServer('BareMinimum',
                  host='localhost',
                  port=5000,
                  brython_version='3.9.1',
                  debug_level=0,
                  )


