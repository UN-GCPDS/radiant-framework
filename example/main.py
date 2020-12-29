from radiant import RadiantAPI, RadiantServer
from browser import document, html
from submodule import submodule_fn


########################################################################
class MainApp(RadiantAPI):

    # ----------------------------------------------------------------------
    def __init__(self, *args, **kwargs):
        """"""
        super().__init__(*args, **kwargs)

        document.select('body')[0] <= html.H1('Hello World')
        submodule_fn()

        document.select('body')[0] <= html.H3(self.MyClass.local_python())


if __name__ == '__main__':
    RadiantServer('MainApp', python=('python_foo.py', 'MyClass'))


