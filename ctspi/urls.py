from django.urls import re_path, path
from ctspi import views
urlpatterns = [
    re_path(r'departments/.*', views.departments),
    re_path(r'\w*', views.main),
    re_path(r'.*', views.ctspi_404),
]
