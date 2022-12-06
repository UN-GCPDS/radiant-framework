from django.views.generic.base import TemplateView
from .models import InternalCall, JointCall, MincienciasCall, StudentsCall


########################################################################
class CallsView(TemplateView):
    template_name = "convocatorias/convocatorias.html"


########################################################################
class InternalCallView(TemplateView):

    # ----------------------------------------------------------------------
    def get(self, request, pk=None, *args, **kwargs):
        """"""
        context = self.get_context_data(**kwargs)

        if pk:
            self.template_name = "convocatorias/internas_view.html"
            context['internalcall'] = InternalCall.objects.get(pk=pk)
            context['internalcall_admin'] = InternalCall._meta
        else:
            self.template_name = "convocatorias/internas.html"
            context['internalcall'] = InternalCall.objects.all()
            context['internalcall_admin'] = InternalCall._meta

        return self.render_to_response(context)



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

    # ----------------------------------------------------------------------
    def get(self, request, pk=None, *args, **kwargs):
        """"""
        context = self.get_context_data(**kwargs)

        if pk:
            self.template_name = "convocatorias/minciencias_view.html"
            context['mincienciascall'] = MincienciasCall.objects.get(pk=pk)
            context['mincienciascall_admin'] = MincienciasCall._meta
        else:
            self.template_name = "convocatorias/minciencias.html"
            context['mincienciascall'] = MincienciasCall.objects.all()
            context['mincienciascall_admin'] = MincienciasCall._meta

        return self.render_to_response(context)



########################################################################
class StudentsCallView(TemplateView):

    # ----------------------------------------------------------------------
    def get(self, request, pk=None, *args, **kwargs):
        """"""
        context = self.get_context_data(**kwargs)

        if pk:
            self.template_name = "convocatorias/estudiantes_view.html"
            context['studentscall'] = StudentsCall.objects.get(pk=pk)
            context['studentscall_admin'] = StudentsCall._meta
        else:
            self.template_name = "convocatorias/estudiantes.html"
            context['studentscall'] = StudentsCall.objects.all()
            context['studentscall_admin'] = StudentsCall._meta

        return self.render_to_response(context)
