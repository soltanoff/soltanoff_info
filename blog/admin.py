# -*- coding: utf-8 -*-
from django.contrib import admin

from blog.models import PostModel


class PostAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title', 'datetime')
    fieldsets = [
        (None, {'fields': ['title']}),
        ('Date information', {'fields': ['datetime'], 'classes': ['expand']}),
        ('Content', {'fields': ['entry', 'content'], 'classes': ['expand']})
    ]


admin.site.register(PostModel, PostAdmin)
