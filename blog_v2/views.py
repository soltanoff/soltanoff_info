from django.views.generic import TemplateView


class ServiceView(TemplateView):
    template_name = "index.html"
