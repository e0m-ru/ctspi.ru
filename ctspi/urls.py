from django.urls import re_path, path, include
from ctspi import views
urlpatterns = [
    path('anons', views.anons),
    path('write_anons', views.write_anons),
    re_path(r'departments/.*', views.departments),
    re_path(r'\w*', views.main),
    re_path(r'.*', views.ctspi_404),
]
