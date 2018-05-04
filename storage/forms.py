# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import gettext_lazy as _


class FileForm(forms.Form):
    title = forms.CharField(label=_("Title:"), required=True)
    notes = forms.CharField(label=_("File notes:"), required=True)
    file = forms.FileField(label=_("Source:"), required=True, widget=forms.FileInput)
