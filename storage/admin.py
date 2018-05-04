# -*- coding: utf-8 -*-
from django.contrib import admin

from storage.models import FileModel


class FileAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title', 'upload_date', 'notes', 'count', 'file')
    fieldsets = [
        (None, {'fields': ['title', 'notes', 'count']}),
        ('Date information', {'fields': ['upload_date'], 'classes': ['collapse']}),
        ('Storage', {'fields': ['file'], 'classes': ['expand']})
    ]


admin.site.register(FileModel, FileAdmin)
