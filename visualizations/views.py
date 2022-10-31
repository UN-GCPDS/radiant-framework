from django.shortcuts import render
from django.views.generic.base import TemplateView
import json
# Create your views here.

from groups.models import ResearchGroup
from researchers.models import Professor

from django.http import HttpResponse, HttpResponseNotFound
from django.views import View

import numpy as np
import textwrap


# ----------------------------------------------------------------------
def break_words(words, width=30, break_='<br>'):
    """"""
    return [break_.join(textwrap.wrap(y_, width=width, break_long_words=False)) for y_ in words]


# ----------------------------------------------------------------------
def fix_filters(model, filters):
    """"""
    if not filters:
        return {}

    for k in filters:
        k_plain = k.replace('~', '')
        filters[k] = [c for c in model._meta.get_field(
            k_plain).choices if filters[k] in c][0][0]

    return filters


########################################################################
class BarsTemplatePlot(TemplateView):
    """"""
    template_name = "empty.html"
    models = {
        'ocde': ResearchGroup,
        'knowledge': ResearchGroup,
        'faculties': ResearchGroup,
        'categories': ResearchGroup,
        'researchers_category': Professor,
        'researchers_faculty': Professor,
        'researchers_departament': Professor,
    }

    # ----------------------------------------------------------------------
    def post(self, request, *args, **kwargs):
        """"""
        # try:
        context = self.get_context_data(**kwargs)
        data = json.loads(request.POST['data'])
        context.update(data)

        if ctx := data['context']:
            plot = ctx
        else:
            plot = data['id'].split('--')[-1]

        context.update(getattr(self, f'render_{plot}')(
            fix_filters(self.models[plot], data['filters'])))

        if context.get('render_plot', False):
            return self.render_to_response(context)
        else:
            return HttpResponse('')
        # except Exception as e:
            # return HttpResponseNotFound('')

    # ----------------------------------------------------------------------
    def render_ocde(self, filters):
        """"""
        self.template_name = "bars.html"
        if 'category' in filters:
            filters.pop('category')
        x, y = zip(*[(ResearchGroup.objects.filter(ocde=key, **filters).count(), label)
                   for key, label in ResearchGroup._meta.get_field('ocde').choices])
        if sum(x) == 0:
            c1, c2, c3 = [], [], []
        else:
            render_plot = True
            x = np.array(x)
            data = np.array([[s.strip() for s in y_.split('|')] for y_ in y])

            # c1 = data[:, 0][np.argwhere(x != 0)[:, 0]].tolist()
            # c3 = data[:, 2][np.argwhere(x != 0)[:, 0]].tolist()
            y_ = np.array(data[:, 1][np.argwhere(x != 0)[:, 0]].tolist())
            x_ = np.array(x[np.argwhere(x != 0)[:, 0]].tolist())
            percentages = [round(100 * xi / sum(x)) for xi in x]

            x = []
            y = []
            for xi, yi in zip(x_, y_):
                if not yi in y:
                    y.append(yi)
                    x.append(sum(x_[np.argwhere(y_ == yi)[:, 0]]))

            y = break_words(y, width=max(map(len, y)) / 2, break_='<br>')
            percentages = [round(100 * xi / sum(x)) for xi in x]

        texttemplate = "%{text}%"
        hovertemplate = "%{x} grupos"

        return locals()

    # ----------------------------------------------------------------------
    def render_knowledge(self, filters):
        """"""
        self.template_name = "bars.html"
        if 'category' in filters:
            filters.pop('category')
        x, y = zip(*[(ResearchGroup.objects.filter(knowledge_area=key, **filters).count(), label)
                   for key, label in ResearchGroup._meta.get_field('knowledge_area').choices])
        if sum(x) == 0:
            x, y = [], []
        else:
            render_plot = True
            x, y = map(list, (zip(*filter(lambda l: l[0], zip(x, y)))))
            percentages = [round(100 * xi / sum(x)) for xi in x]
            y = break_words(y, width=max(map(len, y)) / 2, break_='<br>')

        texttemplate = "%{text}%"
        hovertemplate = "%{x} grupos"

        return locals()

    # ----------------------------------------------------------------------
    def render_faculties(self, filters):
        """"""
        self.template_name = "bars.html"
        x, y = zip(*[(ResearchGroup.objects.filter(faculty=key).count(), label)
                   for key, label in ResearchGroup._meta.get_field('faculty').choices])
        if sum(x) == 0:
            x, y = [], []
        else:
            render_plot = True
            x, y = map(list, (zip(*filter(lambda l: l[0], zip(x, y)))))
            percentages = [round(100 * xi / sum(x)) for xi in x]
            y = break_words(y, width=max(map(len, y)) / 2, break_='<br>')

        texttemplate = "%{text}%"
        hovertemplate = "%{x} grupos"

        return locals()

    # ----------------------------------------------------------------------
    def render_categories(self, filters):
        """"""
        self.template_name = "pie.html"
        if 'category' in filters:
            filters.pop('category')
        x, y = zip(*[(ResearchGroup.objects.filter(category=key, **filters).count(), label)
                   for key, label in ResearchGroup._meta.get_field('category').choices])
        if sum(x) == 0:
            x, y = [], []
        else:
            render_plot = True
            x, y = map(list, (zip(*filter(lambda l: l[0], zip(x, y)))))
            #x = [round(100*xi/sum(x)) for xi in x]

        hovertemplate = "%{value} grupos"

        return locals()

    # ----------------------------------------------------------------------
    def render_researchers_category(self, filters):
        """"""
        if 'category' in filters:
            return {}

        self.template_name = "bars.html"
        x, y = zip(*[(Professor.objects.filter(category=key, **filters).count(), label)
                   for key, label in Professor._meta.get_field('category').choices if label != 'Sin información'])
        if sum(x) == 0:
            x, y = [], []
        else:
            render_plot = True
            x, y = map(list, (zip(*filter(lambda l: l[0], zip(x, y)))))
            percentages = [round(100 * xi / sum(x)) for xi in x]
            # y = break_words(y, width=max(map(len, y)) / 2, break_='<br>')

        texttemplate = "%{text}%"
        hovertemplate = "%{x} grupos"

        return locals()

    # ----------------------------------------------------------------------
    def render_researchers_faculty(self, filters):
        """"""
        if 'faculty' in filters:
            return {}
        if 'departament' in filters:
            return {}

        self.template_name = "bars.html"
        x, y = zip(*[(Professor.objects.filter(faculty=key, **filters).count(), label)
                   for key, label in Professor._meta.get_field('faculty').choices])
        if sum(x) == 0:
            x, y = [], []
        else:
            render_plot = True
            x, y = map(list, (zip(*filter(lambda l: l[0], zip(x, y)))))
            percentages = [round(100 * xi / sum(x)) for xi in x]
            y = break_words(y, width=max(map(len, y)) / 2, break_='<br>')

        texttemplate = "%{text}%"
        hovertemplate = "%{x} grupos"

        return locals()

    # ----------------------------------------------------------------------
    def render_researchers_departament(self, filters):
        """"""
        if 'departament' in filters:
            return {}

        self.template_name = "bars.html"
        x, y = zip(*[(Professor.objects.filter(departament=key, **filters).count(), label)
                   for key, label in Professor._meta.get_field('departament').choices])
        if sum(x) == 0:
            x, y = [], []
        else:
            render_plot = True
            x, y = map(list, (zip(*filter(lambda l: l[0], zip(x, y)))))
            percentages = [round(100 * xi / sum(x)) for xi in x]
            y = break_words(y, width=max(map(len, y)) / 2, break_='<br>')

        texttemplate = "%{text}%"
        hovertemplate = "%{x} grupos"

        return locals()


########################################################################
class GenerateFilteredOptionsView(View):
    """"""

    # ----------------------------------------------------------------------
    def post(self, request, *args, **kwargs):
        """"""
        data = {}
        filters = json.loads(request.POST['filters'])
        filters = fix_filters(ResearchGroup, filters)

        data['groups'] = [str(g[0]) for g in ResearchGroup.objects.filter(**{k: filters[k]
                                                                             for k in ['faculty', 'departament', 'category'] if k in
                                                                             filters}).values_list('pk')]

        departaments = set([d[0] for d in ResearchGroup.objects.filter(**{k: filters[k]
                                                                          for k in ['faculty'] if k in
                                                                          filters}).values_list('departament')])
        data['departaments'] = [dict(ResearchGroup._meta.get_field(
            'departament').choices)[d] for d in departaments]

        return HttpResponse(json.dumps(data), content_type='text/json')
