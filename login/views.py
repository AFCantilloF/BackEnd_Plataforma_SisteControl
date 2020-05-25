from django.shortcuts import render
from .models import Rol, Niveles

# Create your views here.

def inicio(request):
    all_users = Rol.objects.all()
    context = {
        'all_users' : all_users,
    }
    return render(request,"inicio.html",context)

def help(request, user_id):
    return render(request,"help.html")