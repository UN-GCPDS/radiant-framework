from radiant.server import RadiantAPI, RadiantServer
from browser import document, html


########################################################################
class BareMinimum(RadiantAPI):

    # ----------------------------------------------------------------------
    def __init__(self, *args, **kwargs):
        """"""
        super().__init__(*args, **kwargs)
        document.select_one('body') <= html.H1('Hello World')


if __name__ == '__main__':
    RadiantServer('BareMinimum')


