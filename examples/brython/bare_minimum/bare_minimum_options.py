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
        document.select_one('body') <= html.H1('Multipage support')
        document.select_one('body') <= html.A(
            'second page', href='/multipage'
        )

        logging.warning('HOLA')


if __name__ == '__main__':
    RadiantServer(
        'BareMinimum',
        host='localhost',
        port=5000,
        brython_version='3.10.3',
        debug_level=0,
        pages=([r'^/multipage$', 'second_page.Second'],),
    )
