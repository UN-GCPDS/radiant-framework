from django.contrib import admin
from .models import Patent


@admin.register(Patent)
class ResearchGroupAdmin(admin.ModelAdmin):
    list_display = ('filed', 'name', 'patent_type', 'departament')
    list_filter = ('inventors', 'patent_type', 'departament', 'grant', 'filing', 'publication')
    list_display_links = ['filed']
