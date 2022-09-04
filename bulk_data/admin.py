from django.contrib import admin
from .models import ProfessorBulk, GroupsBulk
# Register your models here.


@admin.register(ProfessorBulk)
class ProfessorBulkAdmin(admin.ModelAdmin):
    list_display = ('pk', )


@admin.register(GroupsBulk)
class GroupsBulkAdmin(admin.ModelAdmin):
    list_display = ('pk', )

