from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.conf import settings
from admin_interface.models import Theme

admin.site.unregister(Group)
# admin.site.unregister(User)

if not settings.DEBUG:
    admin.site.unregister(Theme)
