
#!bryhton

from radiant.server import RadiantAPI, RadiantServer
from browser import document, html


########################################################################
class StaticApp(RadiantAPI):

    # ----------------------------------------------------------------------
    def __init__(self, *args, **kwargs):
        """"""
        super().__init__(*args, **kwargs)
        document.select_one('body') <= html.H1('Radiant-Framework')


if __name__ == '__main__':
    RadiantServer('StaticApp',
                  template='layout.html')
