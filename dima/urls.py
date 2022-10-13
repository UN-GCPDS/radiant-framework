from django.urls import path
from django.views.generic import TemplateView
from .views import HomeView, GroupView, NewsletterView, TeamView, PresentationView, MisionView, AvalesView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    # path('admin/default-login/', admin.site.login, name='default-admin-login'),

    path('login/', auth_views.LoginView.as_view(template_name='admin/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('group', GroupView.as_view(), name='group'),
    path('newsletters', NewsletterView.as_view(), name='newsletters'),
    path('equipo_de_trabajo', TeamView.as_view(), name='equipo_de_trabajo'),

    path('presentation', PresentationView.as_view(), name='presentation'),
    # path('presentation', TemplateView.as_view(template_name="presentation.html"), name='presentation'),

    path('mision_y_vision', MisionView.as_view(), name='mision_y_vision'),
    # path('mision_y_vision', TemplateView.as_view(template_name="mission_and_vision.html"), name='mision_y_vision'),


    path('apoyo_proyectos', TemplateView.as_view(), name='apoyo_proyectos'),


    path('avales', AvalesView.as_view(), name='avales'),

    # path('group', GroupView.as_view(), name='group'),
    # path('options', GenerateFilteredOptionsView.as_view(), name='options'),


    # path('test', DashSampleView.as_view(), name='dash_sample'),
    # path('bulk_data', ResearcherView.as_view(), name='researchers'),


]


