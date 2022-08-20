from django.urls import path
from django.views.generic import TemplateView
from research_groups.views import ResearchGroupView, DashSampleView, ResearcherView, CustomTemplateView

urlpatterns = [
    path('', ResearchGroupView.as_view(), name='group'),
    path('test', DashSampleView.as_view(), name='dash_sample'),
    path('researchers', ResearcherView.as_view(), name='researchers'),


    # path('load_template', TemplateView.as_view(template_name="about.html")),
    path('load_template', CustomTemplateView.as_view()),


]


