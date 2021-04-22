from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('registrar/', views.form_empleado, name='registrar_empleado'),
    path('<int:id>/', views.form_empleado, name='modificar_empleado'),
    path('delete/<int:id>/', views.eliminar_empleado, name='eliminar_empleado'),
    path('lista/', views.lista_empleado, name='lista_empleado'),
    path('logout/', views.logout, name="logout"),
    path('home/', views.home, name="home"),
    path('login/', views.login, name="login"),
]