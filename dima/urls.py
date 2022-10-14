from django.urls import path
from django.views.generic import TemplateView
from .views import HomeView, GroupView, NewsletterView, TeamView, ContentView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    # path('admin/default-login/', admin.site.login, name='default-admin-login'),

    path('login/', auth_views.LoginView.as_view(template_name='admin/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('group', GroupView.as_view(), name='group'),
    path('newsletters', NewsletterView.as_view(), name='newsletters'),
    path('equipo_de_trabajo', TeamView.as_view(), name='equipo_de_trabajo'),

    path('presentacion', ContentView.as_view(label='presentation', template_name="presentacion.html"), name='presentation'),
    path('mision_y_vision', ContentView.as_view(label='mision', template_name="mision.html"), name='mision_y_vision'),
    path('avales', ContentView.as_view(label='avales', template_name="avales.html"), name='avales'),
    path('sandbox', ContentView.as_view(label='sandbox', template_name="sandbox.html"), name='sandbox'),

    path('apoyo_proyectos', TemplateView.as_view(), name='apoyo_proyectos'),

    # path('group', GroupView.as_view(), name='group'),
    # path('options', GenerateFilteredOptionsView.as_view(), name='options'),


    # path('test', DashSampleView.as_view(), name='dash_sample'),
    # path('bulk_data', ResearcherView.as_view(), name='researchers'),


]


