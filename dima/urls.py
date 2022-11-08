from django.urls import path
from django.views.generic import TemplateView
from .views import HomeView, NewsletterView, TeamView, ContentView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    # path('admin/default-login/', admin.site.login, name='default-admin-login'),

    path('login/', auth_views.LoginView.as_view(template_name='admin/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),


    # Dynamic
    path('newsletters', NewsletterView.as_view(), name='newsletters'),

    # Static
    path('equipo_de_trabajo', TeamView.as_view(), name='equipo_de_trabajo'),
    path('presentacion', ContentView.as_view(label='presentation',
         template_name="static/presentacion.html"), name='presentation'),
    path('mision_y_vision', ContentView.as_view(label='mision',
         template_name="static/mision.html"), name='mision_y_vision'),
    path('avales', ContentView.as_view(label='avales',
         template_name="static/avales.html"), name='avales'),
    path('contacto', ContentView.as_view(label='contact',
         template_name="static/contact.html"), name='contact'),

    # Convocatorias
    #path('convocatorias_internas', InternalCallView.as_view(), name='internal_call'),
    #path('convocatorias_estudiantes_auxiliares',
    #TemplateView.as_view(), name='calls_aux'),
    #path('busqueda_de_convocatorias',
    #TemplateView.as_view(), name='calls_search'),



    # path('apoyo_proyectos', TemplateView.as_view(), name='apoyo_proyectos'),
    # path('group', GroupView.as_view(), name='group'),
    # path('options', GenerateFilteredOptionsView.as_view(), name='options'),
    # path('test', DashSampleView.as_view(), name='dash_sample'),
    # path('bulk_data', ResearcherView.as_view(), name='researchers'),


]


