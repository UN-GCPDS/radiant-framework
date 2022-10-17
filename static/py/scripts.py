from browser import document, bind, html, window
from dima_scripts import ajax_render, update_plot, ajax_request
import json
import logging

FILTERS_GROUPS = {}
FILTERS_RESEARCHERS = {}


# ----------------------------------------------------------------------
@bind('#dima-select--category__groups', 'change')
def load_group_view(evt):
    """"""
    global FILTERS_GROUPS
    if evt.target.value == 'All':
        FILTERS_GROUPS.pop('category')
    else:
        FILTERS_GROUPS['category'] = evt.target.value

    ajax_render('dima-render--group', "/groups/group", FILTERS_GROUPS)
    update_all_options()


# ----------------------------------------------------------------------
@bind('#dima-select--faculty__groups', 'change')
def update_faculty_filter(evt):
    """"""
    global FILTERS_GROUPS

    if evt.target.value == 'All':
        FILTERS_GROUPS.pop('faculty')
    else:
        FILTERS_GROUPS['faculty'] = evt.target.value

    if 'departament' in FILTERS_GROUPS:
        FILTERS_GROUPS.pop('departament')

    document.select_one(
        '.dima-form__groups #dima-select--departament').value = 'All'
    update_all_plots()
    update_all_options()


# ----------------------------------------------------------------------
@bind('#dima-select--departament__groups', 'change')
def update_departament_filter(evt):
    """"""
    global FILTERS_GROUPS
    if evt.target.value == 'All':
        FILTERS_GROUPS.pop('departament')
    else:
        FILTERS_GROUPS['departament'] = evt.target.value
    update_all_plots()
    update_all_options()


# ----------------------------------------------------------------------
def update_all_plots():
    """"""
    for element in document.select('.dima-plot'):
        update_plot(element.attrs['id'], filters=FILTERS_GROUPS)


# ----------------------------------------------------------------------
def update_all_options(req=None):
    """"""
    if req is None:
        return ajax_request('options', data={'filters': json.dumps(FILTERS_GROUPS), }, callback=update_all_options)

    # Update departaments options
    for option in document.select_one('#dima-select--departament__groups').children[1:]:
        if not option.attrs['value'] in req.json['departaments']:
            option.style = {'display': 'none'}
        else:
            option.style = {'display': 'block'}

    ajax_render('dima-render--group', "/groups/group", FILTERS_GROUPS)


# # ----------------------------------------------------------------------
# @bind(window, 'load')
# def load_researchers_view(evt):
    # """"""
    # ajax_render('investigadores-tab-pane', "/researchers/")

    # # document.select_one('#dima-select--faculty__researchers').addEventListener(
        # # "change", update_faculty_filter_)


# ----------------------------------------------------------------------
@bind('#dima-select--faculty__researchers', 'change')
def update_faculty_filter_(evt):
    """"""
    global FILTERS_RESEARCHERS
    if evt.target.value == 'All':
        FILTERS_RESEARCHERS.pop('faculty')
    else:
        FILTERS_RESEARCHERS['faculty'] = evt.target.value

    if 'departament' in FILTERS_RESEARCHERS:
        FILTERS_RESEARCHERS.pop('departament')

    ajax_render('dima-placeholder__researchers',
                "/researchers/", FILTERS_RESEARCHERS)


# ----------------------------------------------------------------------
@bind('#dima-select--departament__researchers', 'change')
def update_departament_filter_(evt):
    """"""
    global FILTERS_RESEARCHERS
    if evt.target.value == 'All':
        FILTERS_RESEARCHERS.pop('departament')
    else:
        FILTERS_RESEARCHERS['departament'] = evt.target.value

    ajax_render('dima-placeholder__researchers',
                "/researchers/", FILTERS_RESEARCHERS)


# ----------------------------------------------------------------------
@bind('#dima-select--category__researchers', 'change')
def update_researcher_category(evt):
    """"""
    global FILTERS_RESEARCHERS
    if evt.target.value == 'All':
        FILTERS_RESEARCHERS.pop('category')
    else:
        FILTERS_RESEARCHERS['category'] = evt.target.value

    ajax_render('dima-placeholder__researchers',
                "/researchers/", FILTERS_RESEARCHERS)


if __name__.startswith('__main__'):
    update_all_plots()

