from django.shortcuts import render
from django.views.generic.base import TemplateView
import json
# Create your views here.

from research_groups.models import ResearchGroup


# ----------------------------------------------------------------------
def fix_filters(filters):
    """"""
    if not filters:
        return {}

    for k in filters:
        filters[k] = [c for c in ResearchGroup._meta.get_field(k).choices if filters[k] in c][0][0]

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

        context.update(getattr(self, f'render_{plot}')(fix_filters(data['filters'])))
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
        x, y = zip(*[(ResearchGroup.objects.filter(knowledge=key, **filters).count(), label) for key, label in ResearchGroup._meta.get_field('knowledge').choices])
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

