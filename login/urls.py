from django.urls import path, re_path
from . import views

urlpatterns = [
    #/inicio/
    path('', views.inicio, name='inicio'),
    #/inicio/545/
    re_path(r'^(?P<user_id>[0-9]+)/$', 
    views.help, name='help'),
]
