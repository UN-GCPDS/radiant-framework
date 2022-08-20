from research_groups.models import Researcher, ResearchGroup
from django_plotly_dash.models import DashApp, StatelessApp
from django.contrib import admin, auth

# Hide apps from admin
admin.site.unregister(DashApp)
admin.site.unregister(StatelessApp)
admin.site.unregister(auth.models.Group)


@admin.register(Researcher)
class ResearcherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')


@admin.register(ResearchGroup)
class ResearcherAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'leader')

