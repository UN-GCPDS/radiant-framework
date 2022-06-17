from radiant.server import RadiantAPI, RadiantServer
from radiant.sound import Tone

from browser import document, html
from submodule import submodule_fn

from mdc.MDCButton import MDCButton
from mdc.MDCComponent import MDCComponent
from mdc.MDCFormField import MDCForm

import numpy


# from mdc.MDCCard import MDCCard

########################################################################
class MainApp(RadiantAPI):

    # ----------------------------------------------------------------------
    def __init__(self, *args, **kwargs):
        """"""
        super().__init__(*args, **kwargs)

        document.select_one('body') <= html.H1('Hello World')
        document.select_one('body') <= html.A('multipage', href='/multipage')
        submodule_fn()

        document.select_one('body') <= html.H3(self.MyClass.local_python())

        a, b = 3, 5
        c = self.MyClass.pitagoras(a, b)
        document.select_one('body') <= html.H3(
            f"Pitagoras: {a=}, {b=}, {c=:.3f}"
        )

        self.add_css_file('custom_styles.css')

        document <= MDCButton("Button", raised=False, unelevated=True)
        document <= MDCButton("Button raised", raised=True, unelevated=True)
        button = MDCButton(
            "Button outlined", raised=False, outlined=True, unelevated=True
        )
        button.bind('click', self.on_button)

        document <= button

        label = 'SLIDER'
        unit = 'PX'
        id = 'XXXX'

        form = MDCForm()
        label_ = MDCComponent(html.SPAN(f'{label}'))
        label_.mdc.typography('subtitle1')
        form <= label_
        slider_ = form.mdc.Slider('Slider', min=1, max=100, step=5, value=50)

        options = [[f'Option-{o}', f'value-{o}'] for o in range(10)]
        value = 'value-5'
        self.select_ = form.mdc.Select('', options=options, selected=value)

        document.select_one('body') <= form

        document.select_one('body') <= html.I(Class='fas fa-arrow-right')
        document.select_one('body') <= html.I(Class='bi bi-arrow-right')
        document.select_one('body') <= html.SPAN(
            'face', Class='material-icons md-24'
        )

    # ----------------------------------------------------------------------
    def on_button(self, evt):
        """"""
        print(self.select_.mdc.value)


if __name__ == '__main__':
    RadiantServer(
        'MainApp',
        python=('python_foo.py', 'MyClass'),
        handlers=([r'^/ws', ('ws_handler.py', 'WSHandler'), {}],),
        template='custom_template.html',
        mock_imports=['numpy'],
        brython_version='3.9.5',
        debug_level=0,
        pages=([r'^/multipage$', 'second_page.Second'],),
        theme='custom_theme.xml',
    )
