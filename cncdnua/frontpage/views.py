from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "frontpage/index.html"
