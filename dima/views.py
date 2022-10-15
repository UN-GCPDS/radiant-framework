from django.views.generic.base import TemplateView
# Create your views here.
from utils.models import Choices
from groups.models import ResearchGroup
from researchers.models import Researcher, Professor
import json
from visualizations.views import fix_filters
from django.http import HttpResponseNotFound
from .models import Newsletter, Broadcast, Team, Content

from datetime import date


########################################################################
class HomeView(TemplateView):
    template_name = "home.html"

    # ----------------------------------------------------------------------
    def get_context_data(self, **kwargs):
        """"""
        context = super().get_context_data(**kwargs)
        context['groups'] = ResearchGroup.objects.all()
        context['groups_admin'] = ResearchGroup._meta
        context['broadcasts'] = Broadcast.objects.filter(expiration__gt=date.today())
        context['broadcasts_admin'] = Broadcast._meta
        context['faculties'] = Choices.FACULTY
        context['departaments'] = Choices.DEPARTAMENT
        context['categories'] = Choices.GROUPS_CATEGORY

        context['cards'] = [
            ('Grupos de investigación', ResearchGroup.objects.count()),
            ('Departamentos', len(ResearchGroup._meta.get_field('departament').choices)),
            ('Investigadores', Researcher.objects.count() + Professor.objects.exclude(**fix_filters(Professor, {'category': 'Sin información', })).count()),
        ]
        return context


########################################################################
class GroupView(TemplateView):

    # ----------------------------------------------------------------------
    def post(self, request, *args, **kwargs):
        """"""
        self.template_name = "dynamic/groups_table.html"
        context = self.get_context_data(**kwargs)

        filters = fix_filters(ResearchGroup, json.loads(request.POST['data']))
        # context['group'] = ResearchGroup.objects.filter(**data)

        context['groups'] = ResearchGroup.objects.filter(**{k: filters[k]for k in ['faculty', 'departament', 'category'] if k in filters})

        return self.render_to_response(context)

    # ----------------------------------------------------------------------
    def get(self, request, *args, **kwargs):
        """"""
        self.template_name = "dynamic/group_view.html"
        context = self.get_context_data(**kwargs)

        try:
            context['group'] = ResearchGroup.objects.get(pk=request.GET['pk'])
        except:
            return HttpResponseNotFound('<h1>Page not found</h1>')

        return self.render_to_response(context)


########################################################################
class NewsletterView(TemplateView):
    template_name = "dynamic/newsletter.html"

    # ----------------------------------------------------------------------
    def get_context_data(self, **kwargs):
        """"""
        context = super().get_context_data(**kwargs)
        context['newsletters'] = Newsletter.objects.all()
        context['newsletters_admin'] = Newsletter._meta
        return context


########################################################################
class TeamView(TemplateView):
    template_name = "static/equipo_de_trabajo.html"

    # ----------------------------------------------------------------------
    def get_context_data(self, **kwargs):
        """"""
        context = super().get_context_data(**kwargs)
        context['teams'] = Team.objects.all()
        context['teams_admin'] = Team._meta
        return context


########################################################################
class ContentView(TemplateView):
    template_name = ''
    label = ''

    # ----------------------------------------------------------------------
    def get_context_data(self, **kwargs):
        """"""
        context = super().get_context_data(**kwargs)
        context[self.label] = Content.objects.get(label=self.label)
        context[f'{self.label}_admin'] = Content._meta
        return context
