# -*- coding: utf-8 -*-
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.utils.translation import gettext_lazy as _


# TODO: need to the refactoring form
class PostForm(forms.Form):
    title = forms.CharField(label=_("Title:"), required=True)
    entry = forms.CharField(label=_("Entry:"), required=True, widget=CKEditorUploadingWidget(config_name='simple_toolbar'))
    content = forms.CharField(label=_("Content:"), required=True, widget=CKEditorUploadingWidget())
