from django.urls import path
from .views import GroupView

urlpatterns = [
    path('', GroupView.as_view(), name='group'),
    path('<slug:pk>', GroupView.as_view(), name='group'),
]
