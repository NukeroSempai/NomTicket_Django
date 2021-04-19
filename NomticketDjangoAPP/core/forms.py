from django import forms
from .models import empleado

class empleadoForm(forms.ModelForm):
    contraseña=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = empleado
        fields = '__all__'
        
def __init__(self, *args, **kwargs):
    super(empleadoForm,self).__init__(*args, **kwargs)
    self.fields['cargo'].empty_label = "Select"
    
