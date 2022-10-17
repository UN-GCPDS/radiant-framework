from django.views.generic.base import TemplateView
from visualizations.views import fix_filters
from django.http import HttpResponseNotFound
from groups.models import ResearchGroup
import json


########################################################################
class GroupView(TemplateView):

    # ----------------------------------------------------------------------
    def post(self, request, *args, **kwargs):
        """"""
        self.template_name = "groups_table.html"
        context = self.get_context_data(**kwargs)

        filters = fix_filters(
            ResearchGroup, json.loads(request.POST['data']))
        # context['group'] = ResearchGroup.objects.filter(**data)

        context['groups'] = ResearchGroup.objects.filter(
            **{k: filters[k]for k in ['faculty', 'departament', 'category'] if k in filters})
        context['groups_admin'] = ResearchGroup._meta

        return self.render_to_response(context)

    # ----------------------------------------------------------------------
    def get(self, request, pk=None, *args, **kwargs):
        """"""
        self.template_name = "group_view.html"
        context = self.get_context_data(**kwargs)

        try:
            context['group'] = ResearchGroup.objects.get(pk=pk)
            context['group_admin'] = ResearchGroup._meta
        except:
            return HttpResponseNotFound('<h1>Page not found</h1>')

        return self.render_to_response(context)
