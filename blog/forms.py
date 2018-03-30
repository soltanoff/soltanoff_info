# -*- coding: utf-8 -*-
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms


# TODO: need to the refactoring form
class PostForm(forms.Form):
    title = forms.CharField(label="Title:", required=True)
    entry = forms.CharField(label="Entry:", required=True, widget=CKEditorUploadingWidget(config_name='simple_toolbar'))
    content = forms.CharField(label="Content:", required=True, widget=CKEditorUploadingWidget())
