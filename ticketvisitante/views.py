from django.shortcuts import render

# Create your views here.
def login_visitante(request):
    return render(request, 'ticketvisitante/login_visitante.html')

def visitante(request):
    return render(request, 'ticketvisitante/visitante.html')

def ticket_visitante(request):
    return render(request, 'ticketvisitante/ticket_visitante.html')