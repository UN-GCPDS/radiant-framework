from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Professor
from utils.models import Choices
from visualizations.views import fix_filters
from django.http import HttpResponseNotFound
import json


########################################################################
class Researchers(TemplateView):

    # ----------------------------------------------------------------------
    def post(self, request, *args, **kwargs):
        """"""
        self.template_name = "researchers_list.html"
        context = self.get_context_data(**kwargs)

        filters = fix_filters(
            Professor, json.loads(request.POST['data']))

        context['professors'] = Professor.objects.filter(
            **{k: filters[k]for k in ['faculty', 'departament', 'category'] if k in filters})

        context['professors_admin'] = Professor._meta
        return self.render_to_response(context)

    # ----------------------------------------------------------------------
    def get(self, request, pk=None, *args, **kwargs):
        """"""

        self.template_name = "researchers_view.html"
        context = self.get_context_data(**kwargs)

        try:
            context['professor'] = Professor.objects.get(pk=pk)
            context['professor_admin'] = Professor._meta
        except:
            return HttpResponseNotFound('<h1>Page not found</h1>')

        return self.render_to_response(context)
