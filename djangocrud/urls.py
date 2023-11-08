"""
URL configuration for djangocrud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Tareas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Principal,name='Principal'),
    path('Registros/',views.Registro,name='Registro'),
    path('Tareas/',views.Tareas, name='Tareas'),
    path('Tareas_completas/',views.Tareas_completadas, name='Tareas_completadas'),

    path('Tareas/Crear/',views.Crear_Tarea, name='Crear_Tarea'),
    path('Tareas/<int:tarea_id>/',views.Detalles_de_Tarea, name='Detalles_de_Tarea'), #esto es para que devieva distintas url
    path('Tareas/<int:tarea_id>/completada',views.Tarea_Completada, name='Tarea_Completada'),
    path('Tareas/<int:tarea_id>/borrar',views.borrar_tarea, name='borrar_tarea'), 
    path('Cerrar_Sesion/',views.Cerrar_Sesion, name='Cerrar_Sesion'),
    path('Iniciar_Sesion/',views.Iniciar_Sesion, name='Iniciar_Sesion'),
]
