from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.conf import settings
from admin_interface.models import Theme
from .models import Newsletter, Broadcast

admin.site.unregister(Group)
# admin.site.unregister(User)

if not settings.DEBUG:
    admin.site.unregister(Theme)


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('file', 'upload')
    exclude = ('thumbnail',)


@admin.register(Broadcast)
class BroadcastAdmin(admin.ModelAdmin):
    list_display = ('title', 'upload', 'dominant')
    list_display_links = ['title']
