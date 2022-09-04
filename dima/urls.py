from django.urls import path
from django.views.generic import TemplateView
from .views import HomeView, GroupView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('group', GroupView.as_view(), name='group'),

    path('presentation', TemplateView.as_view(template_name="presentation.html")),
    path('mision_y_vision', TemplateView.as_view(template_name="mission_and_vision.html")),
    path('apoyo_proyectos', TemplateView.as_view(template_name="apoyo_proyectos.html")),
    path('equipo_de_trabajo', TemplateView.as_view(template_name="equipo_de_trabajo.html")),

    # path('group', GroupView.as_view(), name='group'),
    # path('options', GenerateFilteredOptionsView.as_view(), name='options'),


    # path('test', DashSampleView.as_view(), name='dash_sample'),
    # path('bulk_data', ResearcherView.as_view(), name='researchers'),


]


