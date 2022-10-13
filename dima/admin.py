from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.conf import settings
from admin_interface.models import Theme
from .models import Newsletter, Broadcast, Team, Content

admin.site.unregister(Group)
# admin.site.unregister(User)

if not settings.DEBUG:
    admin.site.unregister(Theme)


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('file', 'upload')
    exclude = ('thumbnail',)
    list_display_links = ['file']


@admin.register(Broadcast)
class BroadcastAdmin(admin.ModelAdmin):
    list_display = ('upload', 'expiration', 'title', 'link')
    list_display_links = ['upload']


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('area',)
    list_display_links = ['area']


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('label', 'content',)
    list_display_links = ['label']
