from django.db import models

# Create your models here.

# Tabla Comuna
class comuna(models.Model):
    id_comuna = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre',max_length=50,null=False,blank=False)    

    class Meta:
        verbose_name = 'Comuna'
        verbose_name_plural = 'Comunas'
        db_table = 'COMUNA'
    
    def __str__(self):
        return self.nombre


# Tabla Empresa
class empresa(models.Model):
    rut_empresa = models.CharField('Rut Empresa',max_length=15,primary_key=True)
    rsocial_empresa = models.CharField('Razon Social Empresa',max_length=30,null=False,blank=False)
    direccion_empresa = models.CharField('Direccion Empresa',max_length=30,null=True)
    fk_comuna = models.ForeignKey(comuna,on_delete=models.PROTECT,null=False) #no se puede borrar una empresa, si existe una comuna. (primero debe existir una comuna)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        db_table = 'EMPRESA'
    
    def __str__(self):
        return self.rut_empresa + ' - ' + self.rsocial_empresa

#Tabla Sucursal
class sucursal(models.Model):
    id_sucursal = models.AutoField(primary_key=True)
    nom_sucursal = models.CharField('Nombre Sucursal',max_length=15,null=False,blank=False)
    fk_empresa = models.ForeignKey(empresa, on_delete=models.PROTECT,null=False) #no puede existir una sucursal que no tenga una empresa. (debe existir la empresa primero)

    class Meta:
        verbose_name = 'Sucursal'
        verbose_name_plural = 'Sucursales'
        db_table = 'SUCURSAL'

    def __str__(self):
        return self.nom_sucursal

#Tabla Casino
class casino(models.Model):
    rut_casino = models.CharField('Rut Casino',max_length=15,primary_key=True)
    rsocial_casino = models.CharField('Razon Social Casino',max_length=30,null=False,blank=False)
    dir_casino = models.CharField('Direccion Casino',max_length=30,null=False,blank=False)
    fk_sucursal = models.ForeignKey(sucursal,on_delete=models.PROTECT,null=False,blank=False) #no puede existir un casino si no existe la sucursal primero (debe existir la sucursal primero)

    class Meta:
        verbose_name = 'Casino'
        verbose_name_plural = 'Casinos'
        db_table = 'CASINO'

    def __str__(self):
        return self.rsocial_casino

#Tabla Comedor
class comedor(models.Model):
    id_comedor = models.AutoField(primary_key=True)
    nom_comedor = models.CharField('Nombre Comedor',max_length=15,null=False,blank=False)
    fk_casino = models.ForeignKey(casino,on_delete=models.PROTECT,null=False) #no puede existir un comedor si no existe un casino primero (debe existir el casino primero)

    class Meta:
        verbose_name = 'Comedor'
        verbose_name_plural = 'Comedores'
        db_table = 'COMEDOR'

    def __str__(self):
        return self.nom_comedor

#Tabla Producto
#falta agregar archivos de imagenes, si fuese necesario.
class producto(models.Model):
    cod_prod = models.IntegerField('Codigo Producto',primary_key=True,null=False,blank=False)
    nom_prod = models.CharField('Nombre Producto',max_length=15,null=False,blank=False)
    des_prod = models.CharField('Descripcion',max_length=30,null=True)
    precio_prod = models.PositiveIntegerField('Precio',null=False,blank=False,default=0) #validacion en el modelo para que no se ingresen valores negativos

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table = 'PRODUCTO'

    def __str__(self):
        return self.nom_prod

#Tabla Intermedia Producto y comedores
class producto_comedor(models.Model):
    fk_comedor = models.OneToOneField(comedor,on_delete=models.PROTECT,null=False)
    fk_producto = models.ForeignKey(producto,on_delete=models.PROTECT,null=False)
    cantidad = models.PositiveIntegerField('Cantidad',null=False,blank=False,default=0) #validacion en el modelo para que no se ingresen valores negativos

    class Meta:
        verbose_name = 'Inventario comedor'
        verbose_name_plural = 'Inventario comedores'
        db_table = 'PRODUCTOS_COMEDOR'



#Tabla Pedido casino
class pedido_casino(models.Model):
    cod_pedido = models.AutoField(primary_key=True)
    fec_pedido = models.DateField('Fecha de pedido',auto_now=False,auto_now_add=True,null=False)

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        db_table = 'PEDIDO_CASINO'
    
    def __str__(self):
        return self.fec_pedido + ' Codigo = ' + self.cod_pedido

#Tabla Intermedia pedido casino y producto
class pedido_producto(models.Model):
    fk_pedido_casino = models.ForeignKey(pedido_casino,on_delete=models.PROTECT,null=False) #clave foranea pedido casino
    fk_producto = models.ForeignKey(producto,on_delete=models.PROTECT,null=False,blank=False) #clave foranea de producto
    cantidad = models.PositiveIntegerField('Cantidad',null=False,blank=False,default=0)

    class Meta:
        verbose_name = 'pedido de producto'
        verbose_name_plural = 'pedido  de productos'
        db_table = 'PEDIDO_PRODUCTOS'

#Tabla Ticket
class ticket(models.Model):
    cod_ticket = models.AutoField(primary_key=True)
    fecha_imp = models.DateField('Fecha de impresion',auto_now=False,auto_now_add=True,null=False)
    hora_vig_inicio = models.CharField('vigencia Hora Inicio',null=False,max_length=5)
    hora_vig_termino = models.CharField('vigencia Hora Termino',null=False,max_length=5)

    class Meta:
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'
        db_table = 'TICKET'
    
    def __str__(self):
        return self.cod_ticket + 'Fecha: ' + self.fecha_imp

#Tabla Forma de pago
class forma_pago(models.Model):
    cod_forma_pago = models.AutoField(primary_key=True)
    nom_forma_pago = models.CharField('Nombre forma de pago',max_length=30,null=False,blank=False)

    class Meta:
        verbose_name = 'Forma de pago'
        verbose_name_plural = 'Formas de pago'
        db_table = 'FORMA_PAGO'

    def __str__(self):
        return self.nom_forma_pago

#Tabla boleta
class boleta(models.Model):
    num_boleta = models.AutoField(primary_key=True)
    fec_boleta = models.DateField('fecha de boleta',auto_now=False,auto_now_add=True,null=False)
    valor_total = models.IntegerField('Valor Total',null=False)
    valor_ticket = models.IntegerField('Valor Ticket',null=True,blank=True)
    saldo_por_pagar = models.PositiveIntegerField('Saldo por Pagar',null=False,blank=False,default=0) #evita que el saldo por pagar quede negativo, el valor por defecto siempre sera 0
    fk_pedido_casino = models.ForeignKey(pedido_casino,on_delete=models.PROTECT,null=False) #para generar una boleta , esta debe de existir primero un pedido
    fk_ticket = models.ForeignKey(ticket,on_delete=models.PROTECT,null=False) #para generar una boleta , esta debe de existir primero un ticket
    fk_forma_pago = models.ForeignKey(forma_pago,on_delete=models.PROTECT,null=False) #clave foranea de forma de pago, debe existir una forma de pago si o si

    class Meta:
        verbose_name = 'Boleta'
        verbose_name_plural = 'Boletas'
        db_table = 'BOLETA'
    
    def __str__(self):
        return self.num_boleta + 'Total =$ ' + self.valor_total + 'Fecha : ' + self.fec_boleta


#Tabla informe Tickets mensuales
class informe_ticket_mensual(models.Model):
    correlativo_inf = models.AutoField(primary_key=True)
    fecha_proceso = models.DateField('Fecha de proceso',auto_now=False,auto_now_add=True,null=False)
    comedor = models.CharField('Comedor',max_length=15,null=False,blank=False)
    total_boletas = models.PositiveIntegerField(null=False)
    total_tickets = models.PositiveIntegerField(null=False)
    total_ventas = models.PositiveIntegerField(null=False)
    cant_boletas = models.PositiveIntegerField(null=False)
    cant_tickets = models.PositiveIntegerField(null=False)

    class Meta:
        verbose_name = 'Informe'
        verbose_name_plural = 'Informes'
        db_table = 'INFORME_TICKET_MENSUAL'
    
    def __str__(self):
        return self.fecha_proceso + 'Comedor = ' + self.comedor

#Tabla error calc tickets
class error_calc_tickets(models.Model):
    correl_error = models.AutoField(primary_key=True)
    rutina_error = models.CharField('error en',null=False,max_length=150)
    descrip_error = models.CharField('descripcion error',null=False,max_length=200)

    class Meta:
        verbose_name = 'Error de calculo de ticket'
        verbose_name_plural = 'Errores de calculo de tickets'
        db_table = 'ERROR_CALC_TICKET'
    
    def __str__(self):
        return self.correl_error + ' rutina : ' + self.rutina_error

#Tabla tipo usuario
class tipo_usuario(models.Model):
    cod_usuario = models.AutoField(primary_key=True)
    desc_tipo_usuario = models.CharField('Descripcion',max_length=15,null=False,blank=False)

    class Meta:
        verbose_name = 'Tipo de usuario'
        verbose_name_plural = 'Tipos de usuarios'
        db_table = 'TIPO_USUARIO'
    
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
        db_table = 'TURNO'
    
    def __str__(self):
        return self.nom_turno

#Tabla departamento
class departamento(models.Model):
    id_departamento = models.AutoField(primary_key=True)
    nom_departamento = models.CharField('Nombre Departamento',max_length=30,null=False,blank=False)

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        db_table = 'DEPARTAMENTO'
    
    def __str__(self):
        return self.nom_departamento

#Tabla categoria Empleado
class categoria_empleado(models.Model):
    id_categoria_emp = models.AutoField(primary_key=True)
    desc_categoria_emp = models.CharField('Descripcion Categoria Empleado',max_length=30,null=False,blank=False)

    class Meta:
        verbose_name = 'Categoria Empleado'
        verbose_name_plural = 'Categoriass de Empleados'
        db_table = 'CATEGORIA_EMPLEADO'

    def __str__(self):
        return self.desc_categoria_emp

#Tabla Empleado
class empleado(models.Model):
    id_emp = models.AutoField(primary_key=True)
    nom_emp = models.CharField('Nombre',max_length=30,null=False,blank=False)
    appaterno_emp = models.CharField('Apellido paterno',max_length=30,null=False,blank=False)
    apmaterno_emp = models.CharField('Apellido materno',max_length=30,null=False,blank=False)
    numrut_emp = models.IntegerField('rut Empleado sin guion',null=False,blank=False)
    dvrut_emp = models.CharField('Numero verificador',max_length=1,null=False,blank=False)
    direccion_emp = models.CharField('Direccion Empleado',max_length=30,null=False,blank=False)
    email_emp = models.EmailField('Email Empleado',max_length=30,null=False,blank=False)
    tel_emp = models.IntegerField('Numero Empleado',null=False,blank=False)
    sueldo_emp = models.IntegerField('Sueldo Empleado',null=False,blank=False)
    fecha_ingreso = models.DateField('Fecha de ingreso',auto_now=False,auto_now_add=True,null=False)
    password_emp = models.CharField('Contraseña Empleado',max_length=50,null=False,blank=False)
    fk_comuna = models.ForeignKey(comuna,on_delete=models.PROTECT,null=False) #clave foranea de comuna
    fk_categoria_empleado = models.ForeignKey(categoria_empleado,on_delete=models.PROTECT,null=False) #clave foranea categoria empleado
    fk_departamento = models.ForeignKey(departamento,on_delete=models.PROTECT,null=False) #clave  foranea de departamento
    fk_turno = models.ForeignKey(turno,on_delete=models.PROTECT,null=False) #clave foranea de turno
    fk_tipo_usuario = models.ForeignKey(tipo_usuario,on_delete=models.PROTECT,null=False) #clave foranea de tipo usuario

    
    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        db_table = 'EMPLEADO'

    def __str__(self):
        return self.id_emp + 'Nombre = ' + self.nom_emp + ' Apellido = ' + self.appaterno_emp

#Tabla intermedia tickets y empleados para
class tickets_usados(models.Model):
    fk_empleado = models.ForeignKey(empleado,on_delete=models.PROTECT,null=False) #clave foranea de empleado
    fk_ticket = models.OneToOneField(ticket,on_delete=models.PROTECT,null=False) #restriccion que solo 1 ticket puede ser usado a la vez (son unicos)
    fk_turno = models.ForeignKey(turno,on_delete=models.PROTECT,null=False) #relacion turnos 
    fecha = models.DateTimeField(auto_now=False,auto_now_add=True,null=False)

    class Meta:
        verbose_name = 'ticket usado'
        verbose_name_plural ='tickets usados'
        db_table = 'tickets_usados'


#Tabla empleado casino
class empleado_casino(models.Model):
    id_emp_casino = models.AutoField(primary_key=True)
    nom_emp_casino = models.CharField('Nombre',max_length=30,null=False,blank=False)
    appat_emp_casino = models.CharField('Apellido paterno',max_length=30,null=False,blank=False)
    apmat_emp_casino = models.CharField('Apellido materno',max_length=30,null=False,blank=False)
    rut_emp_casino = models.IntegerField('rut Empleado sin guion',null=False,blank=False)
    dv_rut_emp_casino = models.CharField('Numero verificador',max_length=1,null=False,blank=False)
    tel_emp_casino = models.IntegerField('Numero Empleado',null=False,blank=False)
    password_emp_casino = models.CharField('Contraseña Empleado',max_length=50,null=False,blank=False)
    fk_comuna = models.ForeignKey(comuna,on_delete=models.PROTECT,null=False) #clave foranea de comuna
    fk_comedor = models.ForeignKey(comedor,on_delete=models.PROTECT,null=False) #clave foranea de comedor
    
    class Meta:
        verbose_name = 'Empleado Casino'
        verbose_name_plural = 'Casino Empleados'
        db_table = 'EMP_CASINO'
    
    def __str__(self):
        return self.id_emp_casino + 'Nombre = ' + self.nom_emp_casino + ' Apellido = ' + self.appat_emp_casino

