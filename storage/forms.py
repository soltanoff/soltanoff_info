# -*- coding: utf-8 -*-
from django import forms

from storage.models import FileModel


class FileForm(forms.ModelForm):
    class Meta:
        model = FileModel
        fields = ['title', 'notes', 'upload_date', 'file']
