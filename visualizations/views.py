from django.shortcuts import render
from django.views.generic.base import TemplateView
import json
# Create your views here.

from groups.models import ResearchGroup
from django.http import HttpResponse
from django.views import View


# ----------------------------------------------------------------------
def fix_filters(model, filters):
    """"""
    if not filters:
        return {}

    for k in filters:
        k_plain = k.replace('~', '')
        filters[k] = [c for c in model._meta.get_field(k_plain).choices if filters[k] in c][0][0]

    return filters


########################################################################
class BarsTemplatePlot(TemplateView):
    """"""

    # ----------------------------------------------------------------------
    def post(self, request, *args, **kwargs):
        """"""
        context = self.get_context_data(**kwargs)
        data = json.loads(request.POST['data'])
        context.update(data)

        if ctx := data['context']:
            plot = ctx
        else:
            plot = data['id'].split('--')[-1]

        context.update(getattr(self, f'render_{plot}')(fix_filters(ResearchGroup, data['filters'])))
        return self.render_to_response(context)

    # ----------------------------------------------------------------------
    def render_ocde(self, filters):
        """"""
        self.template_name = "bars.html"
        if 'category' in filters:
            filters.pop('category')
        x, y = zip(*[(ResearchGroup.objects.filter(ocde=key, **filters).count(), label) for key, label in ResearchGroup._meta.get_field('ocde').choices])
        if sum(x) == 0:
            x, y = [], []
        else:
            x, y = map(list, (zip(*filter(lambda l: l[0], zip(x, y)))))

        return locals()

    # ----------------------------------------------------------------------
    def render_knowledge(self, filters):
        """"""
        self.template_name = "bars.html"
        if 'category' in filters:
            filters.pop('category')
        x, y = zip(*[(ResearchGroup.objects.filter(knowledge_area=key, **filters).count(), label) for key, label in ResearchGroup._meta.get_field('knowledge_area').choices])
        if sum(x) == 0:
            x, y = [], []
        else:
            x, y = map(list, (zip(*filter(lambda l: l[0], zip(x, y)))))
        return locals()

    # ----------------------------------------------------------------------
    def render_faculties(self, filters):
        """"""
        self.template_name = "bars.html"
        x, y = zip(*[(ResearchGroup.objects.filter(faculty=key).count(), label) for key, label in ResearchGroup._meta.get_field('faculty').choices])
        if sum(x) == 0:
            x, y = [], []
        else:
            x, y = map(list, (zip(*filter(lambda l: l[0], zip(x, y)))))

        return locals()

    # ----------------------------------------------------------------------
    def render_categories(self, filters):
        """"""
        self.template_name = "pie.html"
        if 'category' in filters:
            filters.pop('category')
        x, y = zip(*[(ResearchGroup.objects.filter(category=key, **filters).count(), label) for key, label in ResearchGroup._meta.get_field('category').choices])
        if sum(x) == 0:
            x, y = [], []
        else:
            x, y = map(list, (zip(*filter(lambda l: l[0], zip(x, y)))))

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
        data['departaments'] = [dict(ResearchGroup._meta.get_field('departament').choices)[d] for d in departaments]

        return HttpResponse(json.dumps(data), content_type='text/json')
