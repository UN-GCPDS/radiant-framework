from django.contrib import admin

from .models import InternalCall, JointCall, Timeline, Annex


class TimelineAdmin(admin.StackedInline):
    model = Timeline


class AnnexAdmin(admin.StackedInline):
    model = Annex


@admin.register(InternalCall)
class InternalCallAdmin(admin.ModelAdmin):
    list_display = ('title', 'expiration', 'link', 'active')
    list_display_links = ['title']


@admin.register(JointCall)
class JointCallAdmin(admin.ModelAdmin):
    list_display = ('title', 'expiration', 'link', 'active')
    list_display_links = ['title']
    inlines = [TimelineAdmin, AnnexAdmin]

