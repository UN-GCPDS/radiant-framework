#!bryhton

from radiant.server import RadiantAPI
from browser import document, html
import bootstrap as bs


########################################################################
class Forms(RadiantAPI):

    # ----------------------------------------------------------------------
    def __init__(self, *args, **kwargs):
        """"""
        super().__init__(*args, **kwargs)
        self.add_css_file('styles.css')

        options = (
            {'text': 'A',
             'value': 'a',
             },

            {'text': 'B',
             'value': 'b',
             'selected': True,
             },


            {'text': 'C',
             'value': 'c',
             },


        )

        document.select_one('body') <= bs.form.Select('Hola', options,
                                                      on_change=self.action)

        select = bs.form.Select('Hola', options, on_change=self.action)
        document.select_one('body') <= select
        select.bs.clear()
        select.bs.add_options(options)

    # ----------------------------------------------------------------------
    def action(self, event):
        """"""
        print('HOLA MUNDO')
        print(f'{event.target.value}')

