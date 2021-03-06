from django.contrib import admin
from login.models import Rol,Niveles

# Register your models here.
class NivelesAdmin(admin.ModelAdmin):
    list_display = ('id','nivel')

class RolAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email')
    search_fields = ('nombre','apellido','email')
    list_filter = ('nivel_id',)

admin.site.register(Niveles,NivelesAdmin)
admin.site.register(Rol,RolAdmin)

