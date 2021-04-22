from django import forms
from .models import empleado

class empleadoForm(forms.ModelForm):
    password_emp=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = empleado
        fields = '__all__'
        
class loginEmpForm(forms.ModelForm):
    password_emp=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = empleado
        fields = ['nombreUsuario', 'password_emp']
    
