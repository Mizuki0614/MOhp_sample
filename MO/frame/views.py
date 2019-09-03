from django.views import generic
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from django.core.mail import send_mail

from .models import Inquiry


class IndexPageView(generic.TemplateView):
    template_name = "frame/index.html"


class PortfolioPageView(generic.TemplateView):
    template_name = "frame/portfolio.html"


class PhotographPageView(generic.TemplateView):
    template_name = "frame/photograph.html"


class VideoPageView(generic.TemplateView):
    template_name = "frame/video.html"


class AboutPageView(generic.TemplateView):
    template_name = "frame/about.html"


# 問い合わせフォーム未実装
class ContactPageView(generic.TemplateView):
    template_name = "frame/contact.html"
