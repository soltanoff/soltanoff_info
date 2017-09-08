# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from pyftp.models import FileModel


class FileAdmin(admin.ModelAdmin):
    search_fields = ('file_name',)
    list_display = ('file_name', 'upload_date', 'notes', 'count', 'file')
    fieldsets = [
        (None, {'fields': ['file_name', 'notes', 'count']}),
        ('Date information', {'fields': ['upload_date'], 'classes': ['collapse']}),
        ('Storage', {'fields': ['file'], 'classes': ['expand']})
    ]


admin.site.register(FileModel, FileAdmin)
