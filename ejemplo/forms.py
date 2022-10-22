from django import forms
from ejemplo.models import Persona

class PersonaForm(forms.ModelForm):

    fecha_de_nacimiento = forms.DateField(label="fecha de nacimiento", input_formats=["%d/%m/%Y"],
    #widget es para poder agregar un tip para que el usuario sepa como ingresar la fecha
    widget=forms.TextInput(attrs={'placeholder': '30/12/1995'}))

    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'fecha_de_nacimiento']

