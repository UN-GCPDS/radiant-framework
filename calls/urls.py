from django.urls import path
from .views import InternalCallView, CallsView, JointCallView, MincienciasCallView, StudentsCallView


urlpatterns = [

    path('', CallsView.as_view(), name='calls'),
    path('internas', InternalCallView.as_view(), name='internal_call'),

    path('conjuntas', JointCallView.as_view(), name='joint_call'),
    path('conjuntas/<slug:pk>', JointCallView.as_view(), name='joint_call'),

    path('minciencias', MincienciasCallView.as_view(), name='minciencias_call'),
    path('estudiantes_auxiliares', StudentsCallView.as_view(), name='students_call'),

]


