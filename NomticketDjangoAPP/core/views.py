from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.forms import AuthenticationForm
from .forms import empleadoForm
from .forms import loginEmpForm
from .models import empleado  
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
# Create your views here.

def lista_empleado(request):
    empleados =  empleado.objects.all()
    data = {
        'empleados' : empleados
    }
    return render(request,"CORE/lista_empleado.html", data)

def form_empleado(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = empleadoForm()
        else:
            Empleado = empleado.objects.get(pk=id)
            form = empleadoForm(instance=Empleado)
        return render(request,"CORE/form_empleado.html",{'form':form})
    else:
        if id == 0:
            form = empleadoForm(request.POST)
        else:
            Empleado = empleado.objects.get(pk=id)
            form = empleadoForm(request.POST,instance= Empleado)
        if form.is_valid():
            form.save()
        return redirect('/CORE/lista')
               
def eliminar_empleado(request,id):
    Empleado = empleado.objects.get(pk=id)
    Empleado.delete()
    return redirect('/CORE/lista')

def logout(request): 
    messages.info(request, "Saliste existosamente")
    return redirect("/CORE/")

def login(request):
    if request.method =='POST':
        form = loginEmpForm(request.POST) 
        if form.is_valid:
            nombreUsuario = request.POST['nombreUsuario']
            password_emp = request.POST['password_emp']
            
            verificar = empleado.objects.filter(nombreUsuario=nombreUsuario, password_emp=password_emp).exists()            
            if verificar == True:
                messages.info(request,'WELCOME')
                return redirect('/CORE/home')
            else:
                messages.error(request,'credenciales invalidas')     
                return redirect('/CORE/login')
    else:    
        form = loginEmpForm
        return render(request,"CORE/login.html", {'form':form})

def home(request):
    return render(request,'CORE/home.html')
