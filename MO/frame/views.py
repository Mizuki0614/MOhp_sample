from django.views import generic


class IndexPageView(generic.TemplateView):
    template_name = "frame/index.html"


class PortfolioPageView(generic.TemplateView):
    template_name = "frame/portfolio.html"
