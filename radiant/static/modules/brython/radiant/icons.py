from browser import html

# ----------------------------------------------------------------------
def fa(icon):
    """"""
    if icon.startswith('fa-'):
        icon = icon[3:]
    return html.I(Class=f'fa-solid fa-{icon}')


# ----------------------------------------------------------------------
def bi(icon):
    """"""
    if icon.startswith('bi-'):
        icon = icon[3:]
    return html.I(Class=f'bi bi-{icon}')


# ----------------------------------------------------------------------
def mi(icon, size=48):
    """"""
    if icon.startswith('md-'):
        icon = icon[3:]
    return html.SPAN(icon, Class=f'material-icons md-{size}')
