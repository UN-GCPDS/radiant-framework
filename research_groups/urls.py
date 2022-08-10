from django.urls import path
from research_groups.views import ResearchGroupView

urlpatterns = [
    path('', ResearchGroupView.as_view(), name='group'),
]


