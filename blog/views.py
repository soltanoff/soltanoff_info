# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.views.generic import DetailView

from blog.models import PostModel


class PostDetailView(DetailView):
    model = PostModel


# TODO: blog logic + comment + pages + ajax + picture
@csrf_protect
def index(request):
    search_param = request.GET.get('q', '')

    return render(
        request,
        'blog/index.html',
        {
            'search': search_param,
            'posts': PostModel.objects.all()
        }
    )


@csrf_protect
@login_required
def upload(request):
    title = request.POST.get('title', '')
    entry = request.POST.get('entry', '')
    content = request.POST.get('content', '')
    if title.strip() and entry.strip() and content.strip():
        article = PostModel(title=title, entry=entry, content=content)
        article.save()
        request.file_uploaded = [article.id, article.title]
        return index(request)

    return render(
        request,
        'blog/upload.html',
        {
            'errors': bool(title or entry or content),
            'article_title': title,
            'article_entry': entry,
            'article_content': content
        }
    )
