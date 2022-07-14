#!bryhton

from radiant.server import RadiantAPI
from browser import document, html
import bootstrap as bs


########################################################################
class Buttons(RadiantAPI):

    # ----------------------------------------------------------------------
    def __init__(self, *args, **kwargs):
        """"""
        super().__init__(*args, **kwargs)
        self.add_css_file('styles.css')

        document.select_one('body') <= html.H1('Radiant-Framework: Buttons')
        document.select_one('body') <= html.A('Components', href='/')
        document.select_one('body') <= html.HR()

        for accent in ['primary', 'secondary', 'success', 'danger', 'warning', 'info', 'light', 'dark', 'link']:
            document.select_one('body') <= bs.Button(accent.capitalize(), accent=accent)

        document.select_one('body') <= html.BR()
        document.select_one('body') <= html.BR()
        for tag in ['link', 'button', 'input', 'submit', 'reset']:
            document.select_one('body') <= bs.Button(tag.capitalize(), tag=tag)

        document.select_one('body') <= html.BR()
        document.select_one('body') <= html.BR()
        for accent in ['primary', 'secondary', 'success', 'danger', 'warning', 'info', 'light', 'dark', 'link']:
            document.select_one('body') <= bs.Button(accent.capitalize(), accent=accent, outline=True)

        document.select_one('body') <= html.BR()
        document.select_one('body') <= html.BR()
        for accent in ['primary', 'secondary', 'success', 'danger', 'warning', 'info', 'light', 'dark', 'link']:
            document.select_one('body') <= bs.Button(accent.capitalize(), accent=accent, large=True)

        document.select_one('body') <= html.BR()
        document.select_one('body') <= html.BR()
        for accent in ['primary', 'secondary', 'success', 'danger', 'warning', 'info', 'light', 'dark', 'link']:
            document.select_one('body') <= bs.Button(accent.capitalize(), accent=accent, small=True)

        document.select_one('body') <= html.BR()
        document.select_one('body') <= html.BR()
        for accent in ['primary', 'secondary', 'success', 'danger', 'warning', 'info', 'light', 'dark', 'link']:
            document.select_one('body') <= bs.Button(accent.capitalize(), accent=accent, disabled=True)

        document.select_one('body') <= html.BR()
        document.select_one('body') <= html.BR()
        self.p = []
        for accent in ['primary', 'secondary', 'success', 'danger', 'warning', 'info', 'light', 'dark', 'link']:
            b = bs.Button(accent.capitalize(), accent=accent, toggle=True, Class='to_toggle')
            self.p.append(b)
            document.select_one('body') <= b

        document.select_one('body') <= html.BR()
        document.select_one('body') <= html.BR()
        document.select_one('body') <= bs.Button('Toggle all', 'primary', on_click=self.on_button)

        document.select_one('body') <= html.BR()
        document.select_one('body') <= html.BR()
        group = bs.ButtonGroup()
        for i in range(5):
            group <= bs.Button(f'Button {i}', 'primary')
        document.select_one('body') <= group

        document.select_one('body') <= html.BR()
        document.select_one('body') <= html.BR()
        group2 = bs.ButtonGroup()
        for i in range(5):
            group2.bs.add_button(f'Radio {i}', radio=True, checked=(i == 0))
        document.select_one('body') <= group2

        document.select_one('body') <= html.BR()
        document.select_one('body') <= html.BR()
        group2 = bs.ButtonGroup()
        for i in range(5):
            group2.bs.add_button(f'CHeckbox {i}', checkbox=True)
        document.select_one('body') <= group2

        document.select_one('body') <= html.BR()
        document.select_one('body') <= html.BR()
        tb = bs.ButtonToolbar()

        for j in range(2):
            group2 = bs.ButtonGroup(style={'margin-right': '0.5rem'})
            for i in range(3):
                group2 <= bs.Button(f'Button {i}', 'primary')
            tb <= group2
        document.select_one('body') <= tb

        document.select_one('body') <= html.BR()
        document.select_one('body') <= html.BR()
        group2 = bs.ButtonGroup(vertical=True)
        for i in range(3):
            group2.bs.add_button(f'Radio {i}', radio=True, checked=(i == 0))
        document.select_one('body') <= group2

    # ----------------------------------------------------------------------
    def on_button(self, *args, **kwargs):
        """"""
        for e in self.p:
            print(f'{e}')
            e.bs.toggle()
