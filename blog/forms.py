# -*- coding: utf-8 -*-
from django import forms


# TODO: need to the refactoring form
class PostForm(forms.Form):
    title = forms.CharField(label="Title:", required=True)
    entry = forms.CharField(label="Entry:", required=True, widget=forms.Textarea)
    content = forms.CharField(label="Content:", required=True, widget=forms.Textarea)
