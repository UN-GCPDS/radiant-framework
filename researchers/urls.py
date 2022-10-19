from django.urls import path
from .views import Researchers
urlpatterns = [

    path('', Researchers.as_view(), name='researchers'),
    path('<slug:pk>', Researchers.as_view(), name='researchers'),

]


