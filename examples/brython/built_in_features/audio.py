from radiant.server import RadiantAPI
from radiant.sound import Audio

from browser import document, html

from mdc.MDCButton import MDCButton
from mdc.MDCFormField import MDCSelect


########################################################################
class MainApp(RadiantAPI):

    # ----------------------------------------------------------------------
    def __init__(self, *args, **kwargs):
        """"""
        super().__init__(*args, **kwargs)
        audio = Audio('mixkit-sports-rock-78.mp3')

        style = {
            'margin-top': '25vh',
            'width': '30vw',
            'display': 'grid',
            'grid-auto-flow': 'unset',
            'grid-row-gap': '10px',
            'margin-left': '35vw',
        }
        parent = html.DIV(style=style)

        # select = MDCSelect(
        # 'Tone', note_values.items(), outline=True, selected='B4'
        # )
        play_button = MDCButton("Play", raised=True)
        play_button.bind('click', audio.play)
        parent <= play_button

        pause_button = MDCButton("Pause", raised=True)
        pause_button.bind('click', audio.pause)
        parent <= pause_button

        pause_button = MDCButton("Stop", raised=True)
        pause_button.bind('click', audio.stop)
        parent <= pause_button

        pause_button = MDCButton("Audio-1", raised=True)
        pause_button.bind(
            'click', lambda *args: audio.load('mixkit-sports-rock-78.mp3')
        )
        parent <= pause_button

        pause_button = MDCButton("Audio-2", raised=True)
        pause_button.bind(
            'click', lambda *args: audio.load('mixkit-daredevil-80.mp3')
        )
        parent <= pause_button

        pause_button = MDCButton("0%", raised=True)
        pause_button.bind('click', lambda *args: audio.set_gain(0))
        parent <= pause_button

        pause_button = MDCButton("25%", raised=True)
        pause_button.bind('click', lambda *args: audio.set_gain(0.25))
        parent <= pause_button

        pause_button = MDCButton("50%", raised=True)
        pause_button.bind('click', lambda *args: audio.set_gain(0.5))
        parent <= pause_button

        pause_button = MDCButton("100%", raised=True)
        pause_button.bind('click', lambda *args: audio.set_gain(1))
        parent <= pause_button

        document <= parent


if __name__ == '__main__':
    MainApp()
