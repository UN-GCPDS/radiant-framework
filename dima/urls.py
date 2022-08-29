from django.urls import path
# from django.views.generic import TemplateView
from .views import HomeView, GroupView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('group', GroupView.as_view(), name='group'),

    # path('group', GroupView.as_view(), name='group'),
    # path('options', GenerateFilteredOptionsView.as_view(), name='options'),


    # path('test', DashSampleView.as_view(), name='dash_sample'),
    # path('bulk_data', ResearcherView.as_view(), name='researchers'),


]


