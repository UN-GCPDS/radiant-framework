from django.urls import path
from visualizations.views import BarsTemplatePlot
from .views import GenerateFilteredOptionsView

urlpatterns = [

    # path('load_template', TemplateView.as_view(template_name="about.html")),
    path('load_template', BarsTemplatePlot.as_view()),
    path('options', GenerateFilteredOptionsView.as_view(), name='options'),


]


