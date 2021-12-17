"""myCommServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import include, re_path
from django.contrib import admin
from . import views

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', views.messages, name='messages'),
    re_path(r'^incomingMessage/?$', views.incomingMessage, name='incomingMessage'),
    re_path(r'^outgoingMessage/?$', views.outgoingMessage, name='outgoingMessage'),
    re_path(r'^testSendMessage/?$', views.testSendMessage, name='testSendMessage'),
    re_path(r'^loginUser/?$', views.loginUser, name='loginUser'),
    re_path(r'^logoutUser/?$', views.logoutUser, name='logoutUser'),
    re_path(r'^registerUser/?$', views.registerUser, name='registerUser'),
    re_path(r'^location/?$', views.location, name='location'),
]
