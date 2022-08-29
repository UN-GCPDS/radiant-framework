from django.views.generic.base import TemplateView
# Create your views here.
from utils.models import Choices
from groups.models import ResearchGroup
from researchers.models import Researcher


########################################################################
class HomeView(TemplateView):
    template_name = "home.html"

    # ----------------------------------------------------------------------
    def get_context_data(self, **kwargs):
        """"""
        context = super().get_context_data(**kwargs)
        context['groups'] = ResearchGroup.objects.all()
        context['faculties'] = Choices.FACULTY
        context['departaments'] = Choices.DEPARTAMENT
        context['categories'] = Choices.GROUPS_CATEGORY

        context['cards'] = [
            ('Grupos de investigación', ResearchGroup.objects.count()),
            ('Departamentos', len(ResearchGroup._meta.get_field('departament').choices)),
            ('Investigadores', Researcher.objects.count()),
        ]
        return context


########################################################################
class GroupView(TemplateView):

    # ----------------------------------------------------------------------
    def post(self, request, *args, **kwargs):
        """"""
        self.template_name = "group_table.html"
        context = self.get_context_data(**kwargs)

        data = json.loads(request.POST['data'])
        context['group'] = ResearchGroup.objects.get(**data)

        return self.render_to_response(context)

    # ----------------------------------------------------------------------
    def get(self, request, *args, **kwargs):
        """"""
        self.template_name = "group_view.html"
        context = self.get_context_data(**kwargs)

        id = json.loads(request.GET['pk'])
        context['group'] = ResearchGroup.objects.get(pk=id)

        return self.render_to_response(context)
