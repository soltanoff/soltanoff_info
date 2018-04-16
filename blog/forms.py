# -*- coding: utf-8 -*-
from django import forms

from blog.models import PostModel


class PostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ['title', 'entry', 'content']
