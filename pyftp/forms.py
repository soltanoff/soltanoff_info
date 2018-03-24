# -*- coding: utf-8 -*-
from django import forms


class FileForm(forms.Form):
    file_name = forms.CharField(label="Title:", required=True)
    notes = forms.CharField(label="File notes:", required=True)
    file = forms.FileField(label="Source:", required=True, widget=forms.FileInput)
