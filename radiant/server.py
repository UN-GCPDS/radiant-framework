import sys
from . import RadiantAPI, RadiantServer, RadiantHandler


class fake:
    def __getattr__(self, attr):
        return None


brython = ['browser', 'browser.template']
for module in brython:
    sys.modules[f"{module}"] = fake()

modules = ['sound']
for module in modules:
    sys.modules[f"radiant.{module}"] = fake()

components = ['MDCButton', 'MDCChips', 'MDCDialog', 'MDCFormField', 'MDCIcon',
              'MDCLayoutGrid', 'MDCList', 'MDCShape', 'MDCTab', 'MDCCard',
              'MDCComponent', 'MDCDrawer', 'MDCGridList', 'MDCImageList',
              'MDCLinearProgress', 'MDCMenu', 'MDCSnackbar', 'MDCTopAppBar']
for component in components:
    sys.modules[f"mdc.{component}"] = fake()


