# -*- coding: utf-8 -*-
from datetime import datetime

from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    datetime = models.DateTimeField('Publication date', default=datetime.now)
    content = models.TextField(max_length=10000)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/post/%i/" % self.id
