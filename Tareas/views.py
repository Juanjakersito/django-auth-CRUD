from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm #clase para crear formularios de registrio en django y la otra para autenticarlos
from django.contrib.auth.models import User #clase para regitrar usuarios
from django.contrib.auth import login ,logout,authenticate #clase para autenticar usuarios con cookies y para desregistrarlos el logout y para autenticar los usuarios

from django.http import HttpResponse #importamos metodo para devolver mensaje

from .formularios import TaskForm #Aca importamos el formulario personalizado que creamos

from .models import Tarea #importamos el modelo de las tareas para mostrarlas en la pagina Tareas

from django.utils import timezone #metodo para opteer la hora del computador

from django.contrib.auth.decorators import login_required #esto es para proteger las rutas y que no se puedan meter sin logearse o registrarse


# Create your views here.
@login_required
def Principal(requerimiento):
    return render(requerimiento,'Principal.html')


def Registro(requerimiento):
    if requerimiento.method=='GET':
        return render(requerimiento,'Registro.html',{'formulario':UserCreationForm})
    else:
        if requerimiento.POST['password1']==requerimiento.POST['password2']:
            #registrando el usuario
            try:
                usuario=User.objects.create_user(username=requerimiento.POST['username'],password=requerimiento.POST['password1'])
                usuario.save()
                login(requerimiento,usuario)
                return redirect('Tareas') #para que redireccione al panel de usuario despues de registrarse
            except:
                return render(requerimiento,'Registro.html',{'formulario':UserCreationForm,'error':'El usuario ya existe'})
        else:
            return render(requerimiento,'Registro.html',{'formulario':UserCreationForm,'error':'contrasenias no coinciden'})
@login_required
def Tareas(requerimiento):
    print(requerimiento.POST)
    tareas=Tarea.objects.filter(usuario=requerimiento.user,dia_completada__isnull=True) #aca se filtran las tareas que slo son creadas por el usuario
    return render(requerimiento,'Tareas.html',{'tareas':tareas})
@login_required
def Tareas_completadas(requerimiento):
    print(requerimiento.POST)
    tareas=Tarea.objects.filter(usuario=requerimiento.user,dia_completada__isnull=False) #aca se filtran las tareas que slo son creadas por el usuario
    return render(requerimiento,'Tareas.html',{'tareas':tareas})


@login_required
def Crear_Tarea(requerimiento):


    if requerimiento.method=='GET':
        return render(requerimiento,'Crear_Tarea.html',{'formulario':TaskForm})
    else:
        try:
            formulario=TaskForm(requerimiento.POST)
            nueva_tarea=formulario.save(commit=False) #guardadno los datos optenidos por el metodo post
            nueva_tarea.usuario= requerimiento.user
            nueva_tarea.save()#aca se guarda el dato en la tabla
            print(nueva_tarea)
            print(requerimiento.POST)
            return redirect('Tareas')
        except:
              return render(requerimiento,'Crear_Tarea.html',{'formulario':TaskForm,'error':'Porfavor inserta datos validos'})
@login_required
def Detalles_de_Tarea(requerimiento,tarea_id):

    if requerimiento.method=='GET':
        tarea=get_object_or_404(Tarea,pk=tarea_id,usuario=requerimiento.user) #devuelve la tarea donde el primary key es la id de lla tarea
        formulario= TaskForm(instance=tarea)
        return render(requerimiento,'tarea_detalles.html',{'tarea':tarea,'formulario':formulario})
    else:
        try:
            tarea=get_object_or_404(Tarea,pk=tarea_id)
            formulario=TaskForm(requerimiento.POST,instance=tarea)
            formulario.save()
            return redirect('Tareas')
        except:

           return render(requerimiento,'tarea_detalles.html',{'tarea':tarea,'formulario':formulario,'error':'error al actualizar la tarea'})
@login_required
def Tarea_Completada(requerimiento,tarea_id):
    tarea=get_object_or_404(Tarea,pk=tarea_id,usuario=requerimiento.user)
    if requerimiento.method=='POST':
        tarea.dia_completada=timezone.now() #optenemos fecha  hora actual
        tarea.save()
        return redirect('Tareas')
    




@login_required
def borrar_tarea(requerimiento,tarea_id):
    tarea=get_object_or_404(Tarea,pk=tarea_id,usuario=requerimiento.user)
    if requerimiento.method=='POST':
        tarea.delete()
        return redirect('Tareas')

@login_required
def Cerrar_Sesion(requerimiento):
    logout(requerimiento)
    return redirect('Principal')


def Iniciar_Sesion(requerimiento):
    if requerimiento.method=='GET':
        return render(requerimiento,'Iniciar_Sesion.html',{'autenticacion':AuthenticationForm})
    else:
        usuario=authenticate(requerimiento,username=requerimiento.POST['username'],password=requerimiento.POST['password'])
        if usuario is None:
            print(requerimiento.POST)
            return render(requerimiento,'Iniciar_Sesion.html',{'autenticacion':AuthenticationForm,'error':'usuario o contrasenia invalidos'})
        else:
            login(requerimiento,usuario)
            return redirect('Tareas')
        