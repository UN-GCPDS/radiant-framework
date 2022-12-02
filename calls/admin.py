from django.contrib import admin

from .models import InternalCall, JointCall, MincienciasCall, StudentsCall
from .models import Timeline_InternalCall, TermsOfReference_InternalCall, Annex_InternalCall, Result_InternalCall
from .models import Timeline_JointCall, TermsOfReference_JointCall, Annex_JointCall, Result_JointCall
from .models import TermsOfReference_StudentsCall, Annex_StudentsCall, Result_StudentsCall

##


class Timeline_InternalCallAdmin(admin.StackedInline):
    model = Timeline_InternalCall
    extra = 1


class TermsOfReference_InternalCallAdmin(admin.StackedInline):
    model = TermsOfReference_InternalCall
    extra = 1


class Annex_InternalCallAdmin(admin.StackedInline):
    model = Annex_InternalCall
    extra = 1


class Result_InternalCallAdmin(admin.StackedInline):
    model = Result_InternalCall
    extra = 1

##


class Timeline_JointCallAdmin(admin.StackedInline):
    model = Timeline_JointCall
    extra = 1


class TermsOfReference_JointCallAdmin(admin.StackedInline):
    model = TermsOfReference_JointCall
    extra = 1


class Annex_JointCallAdmin(admin.StackedInline):
    model = Annex_JointCall
    extra = 1


class Result_JointCallAdmin(admin.StackedInline):
    model = Result_JointCall
    extra = 1


##


class TermsOfReference_StudentsCallAdmin(admin.StackedInline):
    model = TermsOfReference_StudentsCall
    extra = 1


class Annex_StudentsCallAdmin(admin.StackedInline):
    model = Annex_StudentsCall
    extra = 1


class Result_StudentsCallAdmin(admin.StackedInline):
    model = Result_StudentsCall
    extra = 1


@admin.register(InternalCall)
class InternalCallAdmin(admin.ModelAdmin):
    list_display = ('title', 'expiration', 'link', 'active')
    list_display_links = ['title']
    inlines = [Timeline_InternalCallAdmin,
               TermsOfReference_InternalCallAdmin,
               Annex_InternalCallAdmin,
               Result_InternalCallAdmin,
               ]


@admin.register(MincienciasCall)
class MincienciasCallAdmin(admin.ModelAdmin):
    list_display = ('title', 'expiration', 'link', 'active')
    list_display_links = ['title']


@admin.register(JointCall)
class JointCallAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'active')
    list_display_links = ['title']
    inlines = [Timeline_JointCallAdmin,
               TermsOfReference_JointCallAdmin,
               Annex_JointCallAdmin,
               Result_JointCallAdmin,
               ]


@admin.register(StudentsCall)
class StudentsCallAdmin(admin.ModelAdmin):
    list_display = ('title', 'expiration', 'supervise', 'active')
    list_display_links = ['title']
    inlines = [TermsOfReference_StudentsCallAdmin,
               Annex_StudentsCallAdmin,
               Result_StudentsCallAdmin,
               ]

