#!bryhton

from radiant.server import RadiantAPI
from browser import document, html

import bootstrap as bt


########################################################################
class BareMinimum(RadiantAPI):

    # ----------------------------------------------------------------------
    def __init__(self, *args, **kwargs):
        """"""
        super().__init__(*args, **kwargs)
        document.select_one('body') <= html.H1('Radiant-Framework')

        for style in ['primary', 'secondary', 'success', 'danger', 'warning', 'info', 'light', 'dark', 'link']:
            document.select_one('body') <= bt.Button(style.capitalize(), style=style)

        document.select_one('body') <= html.BR()
        document.select_one('body') <= html.BR()
        for tag in ['link', 'button', 'input', 'submit', 'reset']:
            document.select_one('body') <= bt.Button(tag.capitalize(), tag=tag)

        document.select_one('body') <= html.BR()
        document.select_one('body') <= html.BR()
        for style in ['primary', 'secondary', 'success', 'danger', 'warning', 'info', 'light', 'dark', 'link']:
            document.select_one('body') <= bt.Button(style.capitalize(), style=style, outline=True)

        document.select_one('body') <= html.BR()
        document.select_one('body') <= html.BR()
        for style in ['primary', 'secondary', 'success', 'danger', 'warning', 'info', 'light', 'dark', 'link']:
            document.select_one('body') <= bt.Button(style.capitalize(), style=style, large=True)

        document.select_one('body') <= html.BR()
        document.select_one('body') <= html.BR()
        for style in ['primary', 'secondary', 'success', 'danger', 'warning', 'info', 'light', 'dark', 'link']:
            document.select_one('body') <= bt.Button(style.capitalize(), style=style, small=True)

        #btn2.bind('click', lambda evt: self.on_button('From Bootstrap'))
        #document.select_one('body') <= btn2

        #document.select_one('body') <= bt.Button('Bootstrap', 'success')

    # ----------------------------------------------------------------------

    def on_button(self, text):
        """"""
        print(f'OUT: {text}')


if __name__ == '__main__':
    BareMinimum()
