#!bryhton

from radiant.server import RadiantAPI
from browser import document, html
import bootstrap as bs


########################################################################
class Dropdowns(RadiantAPI):

    # ----------------------------------------------------------------------
    def __init__(self, *args, **kwargs):
        """"""
        super().__init__(*args, **kwargs)
        self.add_css_file('styles.css')

        document.select_one('body') <= html.H1('Radiant-Framework: Buttons')
        document.select_one('body') <= html.A('Components', href='/')
        document.select_one('body') <= html.HR()

        options = [{'text': f'option-{i}'} for i in range(5)]
        options = [{'header': 'Header', }] + options

        dropdown = bs.Dropdown('Dropdown', options=options)
        document.select_one('body') <= dropdown
        dropdown.bs.add_options([{'divider': True, }, {'text': 'Last option'}])

        document.select_one('body') <= bs.Dropdown('Dropdown split', options=options, split=True)

        document.select_one('body') <= bs.Dropdown('Dropdown', options=options, large=True)

        document.select_one('body') <= bs.Dropdown('Dropdown split', options=options, large=True, split=True)

        document.select_one('body') <= bs.Dropdown('Dropdown', options=options, small=True)

        document.select_one('body') <= bs.Dropdown('Dropdown split', options=options, small=True, split=True)

        document.select_one('body') <= bs.Dropdown('Dark', options=options, dark=True)

        for direction in ['center', 'dropup', 'dropup-center', 'dropend', 'dropstart']:
            document.select_one('body') <= bs.Dropdown(f'Drop - {direction}', options=options, direction=direction)
