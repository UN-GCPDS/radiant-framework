from django.contrib import admin
from researchers.models import Professor, Researcher


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('professor_id', 'first_name', 'last_name')
    list_filter = ('category', 'faculty', 'departament')


@admin.register(Researcher)
class ResearcherAdmin(admin.ModelAdmin):
    list_display = ('researcher_id', 'first_name', 'last_name')

