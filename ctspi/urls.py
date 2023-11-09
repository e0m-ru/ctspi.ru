from django.contrib import admin
from django.urls import re_path
from django.shortcuts import render
from ctspi import views

from django.http import Http404


def custom_404(request, exception):
    return render(request, '404.html', status=404)


handler404 = custom_404

urlpatterns = [
    re_path(r'about', views.main),
    re_path(r'.*', views.main),
]
