from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.views import View

from .plotly_views import sample


from .models import Researcher, ResearchGroup

import pickle


########################################################################
class ResearchGroupView(TemplateView):
    template_name = "groups.html"

    # ----------------------------------------------------------------------
    def get_context_data(self, **kwargs):
        """"""
        context = super().get_context_data(**kwargs)
        # context['groups'] = ResearchGroup.objects.all()

        context['faculties_count'] = [ResearchGroup.objects.filter(faculty=key).count() for key, label in ResearchGroup._meta.get_field('faculty').choices]
        context['faculties'] = [label for key, label in ResearchGroup._meta.get_field('faculty').choices]

        context['ocde_count'] = [ResearchGroup.objects.filter(ocde=key).count() for key, label in ResearchGroup._meta.get_field('ocde').choices]
        context['ocde'] = [label for key, label in ResearchGroup._meta.get_field('ocde').choices]

        context['knowledge_count'] = [ResearchGroup.objects.filter(knowledge=key).count() for key, label in ResearchGroup._meta.get_field('knowledge').choices]
        context['knowledge'] = [label for key, label in ResearchGroup._meta.get_field('knowledge').choices]

        context['category_count'] = [ResearchGroup.objects.filter(category=key).count() for key, label in ResearchGroup._meta.get_field('category').choices]
        context['category'] = [label for key, label in ResearchGroup._meta.get_field('category').choices]

        context['cards'] = [
            ('Grupos de investigación', ResearchGroup.objects.count()),
            ('Departamentos', len(ResearchGroup._meta.get_field('departament').choices)),
            ('Investigadores', Researcher.objects.count()),
        ]

        context['groups'] = ResearchGroup.objects.values_list('id', 'name')

        if group := self.request.GET.dict().get('group', False):
            context['group'] = ResearchGroup.objects.get(id=group)

        return context


########################################################################
class DashSampleView(TemplateView):
    template_name = "sample.html"


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
