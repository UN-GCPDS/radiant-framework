from browser import document, html


# ----------------------------------------------------------------------
def submodule_fn():
    """"""
    document.select_one('body') <= html.H3('Hello from submodule')
