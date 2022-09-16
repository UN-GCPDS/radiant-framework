from django.contrib import admin
from .models import DatabasesBulk
# Register your models here.


@admin.register(DatabasesBulk)
class DatabasesBulkAdmin(admin.ModelAdmin):
    list_display = ('pk', )

