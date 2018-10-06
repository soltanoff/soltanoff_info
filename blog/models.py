# -*- coding: utf-8 -*-
from datetime import datetime

from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class TagModel(models.Model):
    class Meta:
        ordering = ['title']
        verbose_name = _('Tag')

    title = models.CharField(_('Title'), max_length=255)
    datetime = models.DateTimeField(_('Publication date'), default=datetime.now)
    description = models.TextField(_('Description'), max_length=100000)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


class PostModel(models.Model):
    class Meta:
        ordering = ['-datetime']
        verbose_name = _('Post')

    title = models.CharField(_('Title'), max_length=255)
    datetime = models.DateTimeField(_('Publication date'), default=datetime.now)
    tags = models.ManyToManyField(TagModel, verbose_name=_('Tags'), blank=True)
    entry = RichTextUploadingField(_('Entry'), max_length=2000, config_name='simple_toolbar')
    content = RichTextUploadingField(_('Content'), max_length=100000)
    # TODO: soltanoff: add author
    # author = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('Author'))

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    @property
    def url(self):
        return '/post/%s' % self.pk

    def get_all_content(self):
        return ''.join(map(lambda x: '%s' % str(x), (self.entry, self.content)))
