from django.urls import path
from research_groups.views import ResearchGroupView, DashSampleView

urlpatterns = [
    path('', ResearchGroupView.as_view(), name='group'),
    path('', DashSampleView.as_view(), name='dash_sample'),
]


