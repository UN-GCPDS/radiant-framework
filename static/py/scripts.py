from browser import document, bind, html
from dima_scripts import ajax_render, update_plot, ajax_request
import json

FILTERS = {}


# ----------------------------------------------------------------------
@bind('#dima-select--group', 'change')
def load_group_view(evt):
    """"""
    data = {
        'id': evt.target.value,
    }
    ajax_render('dima-render--group', "/group", data)


# ----------------------------------------------------------------------
@bind('#dima-select--category', 'change')
def load_group_view(evt):
    """"""
    global FILTERS
    if evt.target.value == 'All':
        FILTERS.pop('category')
    else:
        FILTERS['category'] = evt.target.value

    update_all_options()


# ----------------------------------------------------------------------
@bind('#dima-select--faculty', 'change')
def update_faculty_filter(evt):
    """"""
    global FILTERS
    if evt.target.value == 'All':
        FILTERS.pop('faculty')
    else:
        FILTERS['faculty'] = evt.target.value

    if 'departament' in FILTERS:
        FILTERS.pop('departament')

    document.select_one('#dima-select--departament').value = 'All'
    update_all_plots()
    update_all_options()


# ----------------------------------------------------------------------
@bind('#dima-select--departament', 'change')
def update_departament_filter(evt):
    """"""
    global FILTERS
    if evt.target.value == 'All':
        FILTERS.pop('departament')
    else:
        FILTERS['departament'] = evt.target.value
    update_all_plots()
    update_all_options()


# ----------------------------------------------------------------------
def update_all_plots():
    """"""
    for element in document.select('.dima-plot'):
        update_plot(element.attrs['id'], filters=FILTERS)


# ----------------------------------------------------------------------
def update_all_options(req=None):
    """"""
    if req is None:
        return ajax_request('options', data={'filters': json.dumps(FILTERS), }, callback=update_all_options)

    # Update departaments options
    for option in document.select_one('#dima-select--departament').children[1:]:
        if not option.attrs['value'] in req.json['departaments']:
            option.style = {'display': 'none'}
        else:
            option.style = {'display': 'block'}

    # Update groups options
    for option in document.select_one('#dima-select--group').children[1:]:
        if not option.attrs['value'] in req.json['groups']:
            option.style = {'display': 'none'}
        else:
            option.style = {'display': 'block'}

    document.select_one('#dima-select--group').value = 'All'


if __name__.startswith('__main__'):
    update_all_plots()

