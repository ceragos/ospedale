from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class StarterTemplateView(TemplateView):
    template_name = 'core/starter-template.html'


class NavbarFixedTemplateView(TemplateView):
    template_name = 'core/base/navbar-fixed.html'


class NavbarStaticTemplateView(TemplateView):
    template_name = 'core/base/navbar-static.html'


class AlbumTemplateView(TemplateView):
    template_name = 'core/album.html'


class CheckoutTemplateView(TemplateView):
    template_name = 'core/checkout.html'


class CarouselTemplateView(TemplateView):
    template_name = 'core/carousel.html'


class SignInTemplateView(TemplateView):
    template_name = 'core/sign-in.html'


class DashboardTemplateView(TemplateView):
    template_name = 'core/dashboard.html'


class JumbotronTemplateView(TemplateView):
    template_name = 'core/jumbotron.html'
