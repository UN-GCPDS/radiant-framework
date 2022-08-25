from django.urls import path
from visualizations.views import BarsTemplatePlot

urlpatterns = [

    # path('load_template', TemplateView.as_view(template_name="about.html")),
    path('load_template', BarsTemplatePlot.as_view()),


]


