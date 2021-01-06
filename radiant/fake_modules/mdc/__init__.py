import sys


class fake:
    def __getattr__(self, attr):
        return None


components = ['MDCButton', 'MDCChips', 'MDCDialog', 'MDCFormField', 'MDCIcon',
              'MDCLayoutGrid', 'MDCList', 'MDCShape', 'MDCTab', 'MDCCard',
              'MDCComponent', 'MDCDrawer', 'MDCGridList', 'MDCImageList',
              'MDCLinearProgress', 'MDCMenu', 'MDCSnackbar', 'MDCTopAppBar']

for component in components:
    sys.modules[f"mdc.{component}"] = fake()


