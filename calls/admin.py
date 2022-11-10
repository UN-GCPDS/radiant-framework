from django.contrib import admin

from .models import InternalCall, JointCall, Timeline, Annex, TermsOfReference, Results


class TimelineAdmin(admin.StackedInline):
    model = Timeline
    extra = 1


class AnnexAdmin(admin.StackedInline):
    model = Annex
    extra = 1


class TermsOfReferenceAdmin(admin.StackedInline):
    model = TermsOfReference
    extra = 1


class ResultsAdmin(admin.StackedInline):
    model = Results
    extra = 1


@admin.register(InternalCall)
class InternalCallAdmin(admin.ModelAdmin):
    list_display = ('title', 'expiration', 'link', 'active')
    list_display_links = ['title']


@admin.register(JointCall)
class JointCallAdmin(admin.ModelAdmin):
    list_display = ('title', 'expiration', 'link', 'active')
    list_display_links = ['title']
    inlines = [TimelineAdmin, TermsOfReferenceAdmin, AnnexAdmin, ResultsAdmin]

