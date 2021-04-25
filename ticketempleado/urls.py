from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.empleado, name="empleado"),
    url(r'^tickets-emitidos', views.tickets_emitidos, name="tickets-emitidos"),
    url(r'^login-empleado', views.login_empleado, name="login-empleado"),
    url(r'^ticket-empleado', views.ticket_empleado, name="ticket-empleado"),
]