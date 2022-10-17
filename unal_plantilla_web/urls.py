from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('legacy', TemplateView.as_view(template_name="base_unal.html")),
]



