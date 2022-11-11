from django.contrib import admin

from .models import InternalCall, JointCall, MincienciasCall, StudentsCall
from .models import Timeline, TermsOfReference, Annex, Result
from .models import TermsOfReferenceS, AnnexS, ResultS


class TimelineAdmin(admin.StackedInline):
    model = Timeline
    extra = 1


class AnnexAdmin(admin.StackedInline):
    model = Annex
    extra = 1


class TermsOfReferenceAdmin(admin.StackedInline):
    model = TermsOfReference
    extra = 1


class ResultAdmin(admin.StackedInline):
    model = Result
    extra = 1


class AnnexSAdmin(admin.StackedInline):
    model = AnnexS
    extra = 1


class TermsOfReferenceSAdmin(admin.StackedInline):
    model = TermsOfReferenceS
    extra = 1


class ResultSAdmin(admin.StackedInline):
    model = ResultS
    extra = 1


@admin.register(InternalCall)
class InternalCallAdmin(admin.ModelAdmin):
    list_display = ('title', 'expiration', 'link', 'active')
    list_display_links = ['title']


@admin.register(MincienciasCall)
class MincienciasCallAdmin(admin.ModelAdmin):
    list_display = ('title', 'expiration', 'link', 'active')
    list_display_links = ['title']


@admin.register(JointCall)
class JointCallAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'active')
    list_display_links = ['title']
    inlines = [TimelineAdmin, TermsOfReferenceAdmin, AnnexAdmin, ResultAdmin]


@admin.register(StudentsCall)
class StudentsCallAdmin(admin.ModelAdmin):
    list_display = ('title', 'expiration', 'supervise', 'active')
    list_display_links = ['title']
    inlines = [TermsOfReferenceSAdmin, AnnexSAdmin, ResultSAdmin]

