from django.urls import path
from .views import InternalCallView


urlpatterns = [

    path('convocatorias_internas', InternalCallView.as_view(), name='internal_call'),

]


