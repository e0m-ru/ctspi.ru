
from django.contrib import admin
from django.urls import path, re_path, include
from django.shortcuts import render
from django.contrib.auth import views as auth_views

def custom_404(request, exception):
    return render(request, '404.html', status=404)

handler404 = custom_404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    re_path('', include('ctspi.urls')),
]
