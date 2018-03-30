# -*- coding: utf-8 -*-
from datetime import datetime

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


class PostModel(models.Model):
    title = models.CharField(max_length=255)
    datetime = models.DateTimeField('Publication date', default=datetime.now)
    entry = models.TextField(max_length=2000, default='')
    content = RichTextUploadingField(max_length=100000)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def getUrl(self):
        return '/post/%s' % self.id

    def getAllContent(self):
        return ''.join(map(lambda x: '%s' % str(x), (self.entry, self.content)))
