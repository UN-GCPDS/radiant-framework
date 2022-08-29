from django.contrib import admin
from .models import ResearchGroup


@admin.register(ResearchGroup)
class ResearchGroupAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)

