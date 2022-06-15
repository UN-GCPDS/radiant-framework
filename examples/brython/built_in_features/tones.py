from radiant.server import RadiantAPI
from radiant.sound import Tone, note_values

from browser import document, html

from mdc.MDCButton import MDCButton
from mdc.MDCFormField import MDCSelect


########################################################################
class MainApp(RadiantAPI):

    # ----------------------------------------------------------------------
    def __init__(self, *args, **kwargs):
        """"""
        super().__init__(*args, **kwargs)
        tone = Tone()

        style = {
            'margin-top': '25vh',
            'width': '30vw',
            'display': 'grid',
            'grid-auto-flow': 'unset',
            'grid-row-gap': '10px',
            'margin-left': '35vw',
        }
        parent = html.DIV(style=style)

        select = MDCSelect(
            'Tone', note_values.items(), outline=True, selected='B4')
        play_button = MDCButton("Play", raised=True)
        play_button.bind('click', lambda evt: tone(
            float(select.mdc.value), 100, 0.5))

        parent <= select
        parent <= play_button

        document <= parent


if __name__ == '__main__':
    MainApp()


