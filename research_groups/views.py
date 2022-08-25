from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.views import View

from .models import Researcher, ResearchGroup

from visualizations.views import fix_filters

import pickle
import json


########################################################################
class HomeView(TemplateView):
    template_name = "groups.html"

    # ----------------------------------------------------------------------
    def get_context_data(self, **kwargs):
        """"""
        context = super().get_context_data(**kwargs)
        context['groups'] = ResearchGroup.objects.all()
        context['faculties'] = ResearchGroup.FACULTIES
        context['departaments'] = ResearchGroup.DEPARTAMENTS
        context['categories'] = ResearchGroup.CATEGORIES

        context['cards'] = [
            ('Grupos de investigación', ResearchGroup.objects.count()),
            ('Departamentos', len(ResearchGroup._meta.get_field('departament').choices)),
            ('Investigadores', Researcher.objects.count()),
        ]
        return context


########################################################################
class DashSampleView(TemplateView):
    template_name = "sample.html"


########################################################################
class GroupView(TemplateView):

    # ----------------------------------------------------------------------
    def post(self, request, *args, **kwargs):
        """"""
        self.template_name = "group_summary.html"
        context = self.get_context_data(**kwargs)

        data = json.loads(request.POST['data'])
        context['group'] = ResearchGroup.objects.get(**data)

        return self.render_to_response(context)

    # ----------------------------------------------------------------------
    def get(self, request, *args, **kwargs):
        """"""
        self.template_name = "group_view.html"
        context = self.get_context_data(**kwargs)

        id = json.loads(request.GET['id'][0])
        context['group'] = ResearchGroup.objects.get(id=id)

        return self.render_to_response(context)


########################################################################
class GenerateFilteredOptionsView(View):
    """"""

    # ----------------------------------------------------------------------
    def post(self, request, *args, **kwargs):
        """"""
        data = {}
        filters = json.loads(request.POST['filters'])
        filters = fix_filters(filters)

        data['groups'] = [str(g[0]) for g in ResearchGroup.objects.filter(**{k: filters[k]
                                                                             for k in ['faculty', 'departament', 'category'] if k in
                                                                             filters}).values_list('id')]

        departaments = set([d[0] for d in ResearchGroup.objects.filter(**{k: filters[k]
                                                                          for k in ['faculty'] if k in
                                                                          filters}).values_list('departament')])
        data['departaments'] = [dict(ResearchGroup._meta.get_field('departament').choices)[d] for d in departaments]

        return HttpResponse(json.dumps(data), content_type='text/json')


########################################################################
class ResearcherView(View):

    # ----------------------------------------------------------------------
    def get(self, request, *args, **kwargs):
        # Perform io-blocking view logic using await, sleep for example.

        groups = pickle.load(open('/home/yeison/Development/Dima/dimawebapp/research_groups/assets/groups.pickle', 'rb'))

        for group in groups:

            members = []

            for member in group.pop('researchers'):
                if member:
                    m = Researcher(**member)
                    m.save()
                    members.append(m)
                # group['researchers'] = members

            if leader := group.pop('leader'):
                l = Researcher(**leader)
                l.save()
                group['leader'] = l

            for k, d in [('faculty', 'FACULTIES'),
                         ('departament', 'DEPARTAMENTS'),
                         ('category', 'CATEGORIES'),
                         ('sub_ocde', 'SUB_OCDE'),
                         ('ocde', 'OCDE'),
                         ('knowledge', 'KNOWLEDGE'),
                         ]:

                for p, n in ResearchGroup._meta.get_field(k).choices:
                    if group[k] == n:
                        group[k] = p
                        continue

            g = ResearchGroup(**group)
            g.save()
            g.researchers.set(members)
            g.save()

        return HttpResponse("Database created!", content_type='text/json')

