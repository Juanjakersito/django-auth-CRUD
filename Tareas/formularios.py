from django import forms
from .models import Tarea

class TaskForm(forms.ModelForm):
    class Meta:
        model=Tarea
        fields=['titulo','descripcion','importante']
        #usaremos widgets para poder estilizar el cuestionario con boostrap
        widgets={
            'titulo':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escribe un titulo'}),
            'descripcion':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Escribe una descripcion'}),
            'importante':forms.CheckboxInput(attrs={'class':'form-check-input m-auto'})}