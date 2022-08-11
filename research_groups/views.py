from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

from .plotly_views import sample


########################################################################
class ResearchGroupView(TemplateView):
    template_name = "groups.html"

    # ----------------------------------------------------------------------
    def get_context_data(self, **kwargs):
        """"""

        context = super().get_context_data(**kwargs)
        # context['latest_articles'] = Article.objects.all()[:5]
        return context


########################################################################
class DashSampleView(TemplateView):
    template_name = "sample.html"

