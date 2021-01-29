"""ospedale URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from apps.core.views import *

urlpatterns = [
    path('starter_template/', StarterTemplateView.as_view(), name='starter.template'),
    path('navbar_static/', NavbarStaticTemplateView.as_view(), name='navbar.static'),
    path('navbar_fixed/', NavbarFixedTemplateView.as_view(), name='navbar.fixed'),
    path('album/', AlbumTemplateView.as_view(), name='album'),
    path('checkout/', CheckoutTemplateView.as_view(), name='checkout'),
    path('carousel/', CarouselTemplateView.as_view(), name='carousel'),
    path('sign_in/', SignInTemplateView.as_view(), name='sign.in'),
    path('dashboard/', DashboardTemplateView.as_view(), name='dashboard'),
    path('jumbotron/', JumbotronTemplateView.as_view(), name='jumbotron'),
]
