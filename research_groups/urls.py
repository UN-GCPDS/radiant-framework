from django.urls import path
from research_groups.views import ResearchGroupView, DashSampleView, ResearcherView

urlpatterns = [
    path('', ResearchGroupView.as_view(), name='group'),
    path('test', DashSampleView.as_view(), name='dash_sample'),
    path('researchers', ResearcherView.as_view(), name='researchers'),
]


