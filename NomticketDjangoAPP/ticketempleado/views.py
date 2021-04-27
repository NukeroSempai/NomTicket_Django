from django.shortcuts import render
from CORE.models import PRODUCTO

# Create your views here.
def tickets_emitidos(request):
    return render(request, 'ticketempleado/lista_tickets_emitidos.html')

def login_empleado(request):
    return render(request, 'ticketempleado/login_empleado.html')

def empleado(request):
    productos = PRODUCTO.objects.all().order_by('codigo_producto')
    return render(request, 'ticketempleado/empleado.html', {'productos' : productos })

def ticket_empleado(request):
    return render(request, 'ticketempleado/ticket_empleado.html')