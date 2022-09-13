from django.contrib import admin
from .models import ResearchGroup


@admin.register(ResearchGroup)
class ResearchGroupAdmin(admin.ModelAdmin):
    list_display = ('minciencias_code', 'name', 'leader', 'faculty', 'departament', 'category')
    list_filter = ('founded', 'category', 'faculty', 'departament', 'knowledge_area')
    list_display_links = ['minciencias_code', "leader"]


