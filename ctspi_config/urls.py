
from django.contrib import admin
from django.urls import path, re_path, include
from django.shortcuts import render


def custom_404(request, exception):
    return render(request, '404.html', status=404)


handler404 = custom_404

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('', include('ctspi.urls')),
]
