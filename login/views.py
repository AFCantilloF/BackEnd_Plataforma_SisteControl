from .models import Rol, Niveles
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics


# Create your views here.
def formulario(request):    
    return render(request,"formulario.html")

def ingresar(request):
    ingreso = False
    rol_db = 0
    if request.GET["user1"]:
        pasword = request.GET["pasword"]
        ingreso_user = request.GET["user1"]
        user = Rol.objects.get(nombre=ingreso_user)
        pasword_db = user.pasword
        rol_db = user.nivel_id
        if pasword == pasword_db:
            ingreso = True
            context = {
                'user' : user, 
                'ingreso_user': ingreso_user,
                'pasword_db': pasword_db,
                'rol_db': rol_db,
            }
        else:
            rol_db = 0
            context = {
                'user':user,
                'ingreso_user': ingreso_user,
                'pasword_db': "EL PASWORD NO COINCIDE",
                'rol_db': "No aplica"
            }
        return render(request,"ingreso.html",context) 
    else:
        mensaje = "not input"
        return HttpResponse(mensaje)
    #lista = [rol_db, ingreso]
    return rol_db,ingreso

#class login_lista(generics.ListCreateAPIView):
#  queryset = ingresar.objects.all()
#  # serializer_class = login_serializer

    #mensaje = "Usuario: %r"%request.GET["user"]
    #ingreso_pasword = request.GET["pasword"]
    #user = Rol.objects.filter(nombre__icontains=ingreso_user)

def inicio(request):
    all_users = Rol.objects.all()
    context = {'all_users' : all_users,}
    return render(request,"inicio.html",context)

def help(request, user_id):
    return render(request,"help.html")



