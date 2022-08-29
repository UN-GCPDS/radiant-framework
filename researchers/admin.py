from django.contrib import admin
from researchers.models import Professor, Researcher


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('pk', 'first_name', 'last_name')


@admin.register(Researcher)
class ResearcherAdmin(admin.ModelAdmin):
    list_display = ('pk', 'first_name', 'last_name')

