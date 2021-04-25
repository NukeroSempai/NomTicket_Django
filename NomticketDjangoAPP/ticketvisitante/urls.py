from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.visitante, name="visitante"),
    url(r'^login-visitante', views.login_visitante, name="login-visitante"),
    url(r'^ticket-visitante', views.ticket_visitante, name="ticket-visitante"),
]