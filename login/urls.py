from django.urls import path, re_path
from . import views

urlpatterns = [
    #/inicio/
    #path('', views.inicio, name='inicio'),
    #/inicio/545/
    #re_path(r'^user/(?P<user_id>[0-9]+)/$', views.help, name='help'),
    #Ingresar
    path('', views.formulario),
    path('ingresar/', views.ingresar),
    #path('pruba1/', views.login_lista.as_view()),
    ]
