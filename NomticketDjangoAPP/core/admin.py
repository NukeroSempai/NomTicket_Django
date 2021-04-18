from django.contrib import admin
from CORE.models import * 

class producto_comedorAdmin(admin.ModelAdmin):
    list_display=('fk_comedor',"fk_producto","cantidad")
class empleadoAdmin(admin.ModelAdmin):
    list_display=('nom_emp',"appaterno_emp","apmaterno_emp","fk_categoria_empleado")
class productoAdmin(admin.ModelAdmin):
    list_display=('nom_prod','precio_prod','fk_tipo_producto')
    
# Register your models here.

admin.site.register(comuna)
admin.site.register(empresa)
admin.site.register(sucursal)
admin.site.register(casino)
admin.site.register(comedor)
admin.site.register(tipo_producto)
admin.site.register(producto)
admin.site.register(producto_comedor,producto_comedorAdmin)
admin.site.register(forma_pago)
admin.site.register(tipo_usuario)
admin.site.register(departamento)
admin.site.register(categoria_empleado)
admin.site.register(turno)
admin.site.register(empleado,empleadoAdmin)
admin.site.register(empleado_casino)