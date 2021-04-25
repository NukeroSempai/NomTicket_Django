from django.shortcuts import render

# Create your views here.
def tickets_emitidos(request):
    return render(request, 'ticketempleado/lista_tickets_emitidos.html')

def login_empleado(request):
    return render(request, 'ticketempleado/login_empleado.html')

def empleado(request):
    return render(request, 'ticketempleado/empleado.html')

def ticket_empleado(request):
    return render(request, 'ticketempleado/ticket_empleado.html')