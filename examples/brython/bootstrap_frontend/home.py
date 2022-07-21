from radiant.server import RadiantAPI
from browser import document, html
import bootstrap as bs

########################################################################


class Home(RadiantAPI):

    # ----------------------------------------------------------------------
    def __init__(self, *args, **kwargs):
        """"""
        super().__init__(*args, **kwargs)
        self.add_css_file('styles.css')

        document.select_one('body') <= html.H1('Bootstrap')
        document.select_one('body') <= html.HR()

        document.select_one('body') <= bs.Button('Buttons', tag='link', href='/buttons')
        document.select_one('body') <= bs.Button('Dropdowns', tag='link', href='/dropdowns')
        document.select_one('body') <= bs.Button('Forms', tag='link', href='/forms')


