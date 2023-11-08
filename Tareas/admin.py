from django.contrib import admin
from .models import Tarea #importamos la tabla 

class TareaAdmin(admin.ModelAdmin): #esto se aniade para que en lapnel de admin aparezca la fecha de creacion
    readonly_fields=('fecha_de_creacion',)

# Register your models here.
admin.site.register(Tarea,TareaAdmin)
