# -*- coding: utf-8 -*-
from django.contrib import admin

from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title', 'datetime')
    fieldsets = [
        (None, {'fields': ['title']}),
        ('Date information', {'fields': ['datetime'], 'classes': ['expand']}),
        ('Content', {'fields': ['content'], 'classes': ['expand']})
    ]


admin.site.register(Post, PostAdmin)
