from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.visitante, name="visitante"),
    url(r'^login-visitante', views.login_visitante, name="login-visitante"),
]