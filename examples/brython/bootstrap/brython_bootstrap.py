#!bryhton

from radiant.server import RadiantAPI
from browser import document, html

from bootstrap.btn import Button
from mdc.MDCButton import MDCButton


########################################################################
class BareMinimum(RadiantAPI):

    # ----------------------------------------------------------------------
    def __init__(self, *args, **kwargs):
        """"""
        super().__init__(*args, **kwargs)
        document.select_one('body') <= html.H1('Radiant-Framework')

        btn1 = MDCButton("Button", raised=False, unelevated=True)
        btn1.bind('click', lambda evt: self.on_button('From MDC'))
        document.select_one('body') <= btn1

        btn2 = Button('Bootstrap')
        btn2.bind('click', lambda evt: self.on_button('From Bootstrap'))
        document.select_one('body') <= btn2

        document.select_one('body') <= Button('Bootstrap', 'success')

    # ----------------------------------------------------------------------
    def on_button(self, text):
        """"""
        print(f'OUT: {text}')


if __name__ == '__main__':
    BareMinimum()
