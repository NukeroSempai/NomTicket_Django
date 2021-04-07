from django.db import models

# Create your models here.

# Tabla Comuna
class comuna(models.Model):
    id_comuna = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre',max_length=50,null=False,blank=False)

    class Meta:
        verbose_name = 'Comuna'
        verbose_name_plural = 'Comunas'
    
    def __str__(self):
        return self.nombre


# Tabla Empresa
class empresa(models.Model):
    rut_empresa = models.CharField('Rut Empresa',max_length=15,primary_key=True)
    rsocial_empresa = models.CharField('Razon Social Empresa',max_length=30,null=False,blank=False)
    direccion_empresa = models.CharField('Direccion Empresa',max_length=30,null=True)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
    
    def __str__(self):
        return self.rut_empresa + ' - ' + self.rsocial_empresa

#Tabla Sucursal
class sucursal(models.Model):
    id_sucursal = models.AutoField(primary_key=True)
    nom_sucursal = models.CharField('Nombre Sucursal',max_length=15,null=False,blank=False)

    class Meta:
        verbose_name = 'Sucursal'
        verbose_name_plural = 'Sucursales'

    def __str__(self):
        return self.nom_sucursal

#Tabla Casino
class casino(models.Model):
    rut_casino = models.CharField('Rut Casino',max_length=15,primary_key=True)
    rsocial_casino = models.CharField('Razon Social Casino',max_length=30,null=False,blank=False)
    dir_casino = models.CharField('Direccion Casino',max_length=30,null=False,blank=False)

    class Meta:
        verbose_name = 'Casino'
        verbose_name_plural = 'Casinos'

    def __str__(self):
        return self.rsocial_casino

#Tabla Comedor
class comedor(models.Model):
    id_comedor = models.AutoField(primary_key=True)
    nom_comedor = models.CharField('Nombre Comedor',max_length=15,null=False,blank=False)

    class Meta:
        verbose_name = 'Comedor'
        verbose_name_plural = 'Comedores'

    def __str__(self):
        return self.nom_comedor

#Tabla Producto
#falta agregar archivos de imagenes.
class producto(models.Model):
    cod_prod = models.IntegerField('Codigo Producto',primary_key=True,null=False,blank=False)
    nom_prod = models.CharField('Nombre Producto',max_length=15,null=False,blank=False)
    des_prod = models.CharField('Descripcion',max_length=30,null=True)
    precio_prod = models.IntegerField('Precio',null=False)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.nom_prod

#Tabla Pedido casino
class pedido_casino(models.Model):
    cod_pedido = models.AutoField(primary_key=True)
    fec_pedido = models.DateField('Fecha de pedido',auto_now=False,auto_now_add=True,null=False)

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
    
    def __str__(self):
        return self.fec_pedido + ' Codigo = ' + self.cod_pedido

#Tabla boleta
class boleta(models.Model):
    num_boleta = models.AutoField(primary_key=True)
    fec_boleta = models.DateField('fecha de boleta',auto_now=False,auto_now_add=True,null=False)
    valor_total = models.IntegerField('Valor Total',null=False)
    valor_ticket = models.IntegerField('Valor Ticket',null=True)
    saldo_por_pagar = models.IntegerField('Saldo por Pagar',null=True)

    class Meta:
        verbose_name = 'Boleta'
        verbose_name_plural = 'Boletas'
    
    def __str__(self):
        return self.num_boleta + 'Total =$ ' + self.valor_total + 'Fecha : ' + self.fec_boleta

#Tabla Forma de pago
class forma_pago(models.Model):
    cod_forma_pago = models.AutoField(primary_key=True)
    nom_forma_pago = models.CharField('Nombre forma de pago',max_length=30,null=False,blank=False)

    class Meta:
        verbose_name = 'Forma de pago'
        verbose_name_plural = 'Formas de pago'
    def __str__(self):
        return self.nom_forma_pago

#Tabla informe Tickets mensuales
class informe_ticket_mensual(models.Model):
    correlativo_inf = models.AutoField(primary_key=True)
    fecha_proceso = models.DateField('Fecha de proceso',auto_now=False,auto_now_add=True,null=False)
    comedor = models.CharField('Comedor',max_length=15,null=False,blank=False)
    total_boletas = models.IntegerField(max_length=6,null=False)
    total_tickets = models.IntegerField(max_length=9,null=False)
    total_ventas = models.IntegerField(max_length=9,null=False)
    cant_boletas = models.IntegerField(max_length=9,null=False)
    cant_tickets = models.IntegerField(max_length=9,null=False)

    class Meta:
        verbose_name = 'Informe'
        verbose_name_plural = 'Informes'
    
    def __str__(self):
        return self.fecha_proceso + 'Comedor = ' + self.comedor

#Tabla Ticket
class ticket(models.Model):
    cod_ticket = models.AutoField(primary_key=True)
    fecha_imp = models.DateField('Fecha de impresion',auto_now=False,auto_now_add=True,null=False)
    hora_vig_inicio = models.CharField('vigencia Hora Inicio',null=False,max_length=5)
    hora_vig_termino = models.CharField('vigencia Hora Termino',null=False,max_length=5)

    class Meta:
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'
    
    def __str__(self):
        return self.cod_ticket + 'Fecha: ' + self.fecha_imp

#Tabla error calc tickets
class error_calc_tickets(models.Model):
    correl_error = models.AutoField(primary_key=True)
    rutina_error = models.CharField('error en',null=False,max_length=150)
    descrip_error = models.CharField('descripcion error',null=False,max_length=200)

    class Meta:
        verbose_name = 'Error de calculo de ticket'
        verbose_name_plural = 'Errores de calculo de tickets'
    
    def __str__(self):
        return self.correl_error + ' rutina : ' + self.rutina_error

#Tabla tipo usuario
class tipo_usuario(models.Model):
    cod_usuario = models.AutoField(primary_key=True)
    desc_tipo_usuario = models.CharField('Descripcion',max_length=15,null=False,blank=False)

    class Meta:
        verbose_name = 'Tipo de usuario'
        verbose_name_plural = 'Tipos de usuarios'
    
    def __str__(self):
        return self.desc_tipo_usuario

#Tabla turnos
class turno(models.Model):
    id_turno = models.AutoField(primary_key=True)
    nom_turno = models.CharField('Nombre Turno',max_length=15,null=False,blank=False)
    hora_inicio = models.CharField('Hora inicio',max_length=5,null=False,blank=False)
    hora_termino = models.CharField('Hora termino',max_length=5,null=False,blank=False)

    class Meta:
        verbose_name = 'Turno'
        verbose_name_plural ='Turnos'
    
    def __str__(self):
        return self.nom_turno

#Tabla departamento
class departamento(models.Model):
    id_departamento = models.AutoField(primary_key=True)
    nom_departamento = models.CharField('Nombre Departamento',max_length=30,null=False,blank=False)

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
    
    def __str__(self):
        return self.nom_departamento

#Tabla categoria Empleado
class categoria_empleado(models.Model):
    id_categoria_emp = models.AutoField(primary_key=True)
    desc_categoria_emp = models.CharField('Descripcion Categoria Empleado',max_length=30,null=False,blank=False)

    class Meta:
        verbose_name = 'Categoria Empleado'
        verbose_name_plural = 'Categoriass de Empleados'

    def __str__(self):
        return self.desc_categoria_emp

#Empleado
class empleado(models.Model):
    id_emp = models.AutoField(primary_key=True)
    nom_emp = models.CharField('Nombre',max_length=30,null=False,blank=False)
    appaterno_emp = models.CharField('Apellido paterno',max_length=30,null=False,blank=False)
    apmaterno_emp = models.CharField('Apellido materno',max_length=30,null=False,blank=False)
    numrut_emp = models.IntegerField('rut Empleado sin guion',max_length=10,null=False,blank=False)
    dvrut_emp = models.CharField('Numero verificador',max_length=1,null=False,blank=False)
    direccion_emp = models.CharField('Direccion Empleado',max_length=30,null=False,blank=False)
    email_emp = models.EmailField('Email Empleado',max_length=30,null=False,blank=False)
    tel_emp = models.IntegerField('Numero Empleado',max_length=9,null=False,blank=False)
    sueldo_emp = models.IntegerField('Sueldo Empleado',max_length=7,null=False,blank=False)
    fecha_ingreso = models.DateField('Fecha de ingreso',auto_now=False,auto_now_add=True,null=False)
    password_emp = models.CharField('Contraseña Empleado',max_length=10,null=False,blank=False)
    
    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        return self.id_emp + 'Nombre = ' + self.nom_emp + ' Apellido = ' + self.appaterno_emp

#Tabla empleado casino
class empleado_casino(models.Model):
    id_emp_casino = models.AutoField(primary_key=True)
    nom_emp_casino = models.CharField('Nombre',max_length=30,null=False,blank=False)
    appat_emp_casino = models.CharField('Apellido paterno',max_length=30,null=False,blank=False)
    apmat_emp_casino = models.CharField('Apellido materno',max_length=30,null=False,blank=False)
    rut_emp_casino = models.IntegerField('rut Empleado sin guion',max_length=10,null=False,blank=False)
    dv_rut_emp_casino = models.CharField('Numero verificador',max_length=1,null=False,blank=False)
    tel_emp_casino = models.IntegerField('Numero Empleado',max_length=9,null=False,blank=False)
    password_emp_casino = models.CharField('Contraseña Empleado',max_length=10,null=False,blank=False)
    
    class Meta:
        verbose_name = 'Empleado Casino'
        verbose_name_plural = 'Casino Empleados'
    
    def __str__(self):
        return self.id_emp_casino + 'Nombre = ' + self.nom_emp_casino + ' Apellido = ' + self.appat_emp_casino

