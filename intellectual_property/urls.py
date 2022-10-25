from django.urls import path
from .views import PatentsView
urlpatterns = [

    path('patents/', PatentsView.as_view(), name='patents'),
    path('patents/<slug:pk>', PatentsView.as_view(), name='patents'),

]


