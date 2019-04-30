from django.views.generic import TemplateView


class BlogV2View(TemplateView):
    template_name = "index.html"
