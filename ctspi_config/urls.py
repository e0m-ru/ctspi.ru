from django.contrib import admin
from django.urls import path, re_path, include
from django.shortcuts import render
from ctspi import views
from ctspi_config import login_logout

def custom_404(request, exception):
    return render(request, '404.html', status=404)

handler404 = custom_404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_logout.login_view, name='login'),
    path('logout/', login_logout.logout_view, name='login'),
    # path('logout/', MyLogoutView.as_view(), {'next_page': LOGOUT_REDIRECT_URL}, name='logout'),
    re_path('', include('ctspi.urls')),
]
