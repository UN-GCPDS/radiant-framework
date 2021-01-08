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

        document.select('body')[0] <= html.H1('Hello World')
        submodule_fn()

        document.select('body')[0] <= html.H3(self.MyClass.local_python())

        a, b = 3, 5
        c = self.MyClass.pitagoras(a, b)
        document.select('body')[0] <= html.H3(f"Pitagoras: {a=}, {b=}, {c=:.3f}")

        self.add_css_file('custom_styles.css')

        document <= MDCButton("Button", raised=False)
        document <= MDCButton("Button raised", raised=True)
        document <= MDCButton("Button outlined", raised=False, outlined=True)

        label = 'SLIDER'
        unit = 'PX'
        id = 'XXXX'

        form = MDCForm()
        label_ = MDCComponent(html.SPAN(f'{label}'))
        label_ .mdc.typography('subtitle1')
        form <= label_
        form <= MDCComponent(html.SPAN(f' {float(50):.1f} {unit}', id=f'value_{id}')).mdc.typography('caption')
        slider_ = form.mdc.Slider('Slider', min=1, max=100, step=5, value=50)

        document <= form

        # document <= MDCCard("Card title", subtitle="Secondary text", text_content="off")


if __name__ == '__main__':
    RadiantServer('MainApp',
                  python=('python_foo.py', 'MyClass'),
                  handlers=([r'^/ws', ('ws_handler.py', 'WSHandler'), {}], ),
                  template='custom_template.html',
                  mock_imports=['numpy'],
                  # theme='custom_theme.xml',
                  )


