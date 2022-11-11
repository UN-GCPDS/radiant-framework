from django.views.generic.base import TemplateView
from .models import InternalCall, JointCall, MincienciasCall, StudentsCall


########################################################################
class CallsView(TemplateView):
    template_name = "convocatorias/convocatorias.html"


########################################################################
class InternalCallView(TemplateView):
    template_name = "convocatorias/internas.html"

    # ----------------------------------------------------------------------
    def get_context_data(self, **kwargs):
        """"""
        context = super().get_context_data(**kwargs)
        context['internalcall'] = InternalCall.objects.all()
        context['internalcall_admin'] = InternalCall._meta
        return context


########################################################################
class JointCallView(TemplateView):

    # ----------------------------------------------------------------------
    def get(self, request, pk=None, *args, **kwargs):
        """"""
        context = self.get_context_data(**kwargs)

        if pk:
            self.template_name = "convocatorias/conjunta_view.html"
            context['jointcall'] = JointCall.objects.get(pk=pk)
            context['jointcall_admin'] = JointCall._meta
        else:
            self.template_name = "convocatorias/conjuntas.html"
            context['jointcall'] = JointCall.objects.all()
            context['jointcall_admin'] = JointCall._meta

        return self.render_to_response(context)


########################################################################
class MincienciasCallView(TemplateView):
    template_name = "convocatorias/minciencias.html"

    # ----------------------------------------------------------------------
    def get_context_data(self, **kwargs):
        """"""
        context = super().get_context_data(**kwargs)
        context['mincienciascall'] = MincienciasCall.objects.all()
        context['mincienciascall_admin'] = MincienciasCall._meta
        return context


########################################################################
class StudentsCallView(TemplateView):
    template_name = "convocatorias/estudiantes.html"

    # ----------------------------------------------------------------------
    def get_context_data(self, **kwargs):
        """"""
        context = super().get_context_data(**kwargs)
        context['studentscall'] = StudentsCall.objects.all()
        context['studentscall_admin'] = StudentsCall._meta
        return context
