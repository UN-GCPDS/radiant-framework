from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Patent
from utils.models import Choices
from visualizations.views import fix_filters
from django.http import HttpResponseNotFound
import json


########################################################################
class PatentsView(TemplateView):

    # ----------------------------------------------------------------------
    def post(self, request, *args, **kwargs):
        """"""
        self.template_name = "patents_list.html"
        context = self.get_context_data(**kwargs)

        filters = fix_filters(
            Patent, json.loads(request.POST['data']))

        context['patents'] = Patent.objects.filter(
            **{k: filters[k] for k in ['departament', 'patent_type'] if k in filters})        

        context['patents_admin'] = Patent._meta
        return self.render_to_response(context)

    # ----------------------------------------------------------------------
    def get(self, request, pk=None, *args, **kwargs):
        """"""
        self.template_name = "patents_view.html"
        context = self.get_context_data(**kwargs)

        try:
            context['patent'] = Patent.objects.get(pk=pk.replace('-', '/'))
            context['patent_admin'] = Patent._meta
        except:
            return HttpResponseNotFound('<h1>Page not found</h1>')

        return self.render_to_response(context)
