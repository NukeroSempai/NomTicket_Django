from django.contrib import admin
from CORE.models import *

class EMPLEADO_ADMIN(admin.ModelAdmin):
    list_display=("rut_emp","nom_emp","appaterno_emp","apmaterno_emp","fk_perfil")


admin.site.register(PERFIL)
admin.site.register(COMUNA)
admin.site.register(TIPO_TICKET)
admin.site.register(DETALLE_AUDITORIA)
admin.site.register(AUDITORIA)
admin.site.register(TURNO)
admin.site.register(FORMA_PAGO)
admin.site.register(CAJERO)
admin.site.register(EMPLEADO,EMPLEADO_ADMIN)
admin.site.register(TICKET)
admin.site.register(BOLETA)
admin.site.register(DETALLE_BOLETA)
admin.site.register(PRODUCTO)
admin.site.register(TIPO_PRODUCTO)
admin.site.register(ERRORES)
admin.site.register(INFORME_TICKET)
