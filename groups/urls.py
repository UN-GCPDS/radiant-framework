from django.urls import path
from .views import GroupView

urlpatterns = [
    path('<slug:pk>', GroupView.as_view(), name='group'),
]
