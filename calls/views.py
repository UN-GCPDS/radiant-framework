from django.views.generic.base import TemplateView

# Create your views here.
from .models import InternalCall


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
