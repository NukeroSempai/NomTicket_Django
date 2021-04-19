from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import empleadoForm
from .models import empleado  
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
# Create your views here.

def lista_empleado(request):
    empleados =  empleado.objects.all()
    data = {
        'empleados' : empleados
    }
    return render(request,"empleado/lista_empleado.html", data)

def form_empleado(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = empleadoForm()
        else:
            empleado = empleado.objects.get(pk=id)
            form = empleadoForm(instance=empleado)
        return render(request,"empleado/form_empleado.html",{'form':form})
    else:
        if id == 0:
            form = empleadoForm(request.POST)
        else:
            empleado = empleado.objects.get(pk=id)
            form = empleadoForm(request.POST,instance= empleado)
        if form.is_valid():
            form.save()
        return redirect('/empleado/lista')
            
def eliminar_empleado(request,id):
    empleado = empleado.objects.get(pk=id)
    empleado.delete()
    return redirect('/empleado/lista')

def logout(request): 
    messages.info(request, "Saliste existosamente")
    return redirect("/empleado/")

def login(request):
    form = AuthenticationForm 
    return render(request,"empleado/login.html",{"form":form})

def home(request):
    return render(request,"empleado/home.html")
