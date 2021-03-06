# Generated by Django 3.1.2 on 2021-04-24 03:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AUDITORIA',
            fields=[
                ('correlativo_aud', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_auditoria', models.DateField(auto_now_add=True, verbose_name='fecha auditoria')),
            ],
            options={
                'verbose_name': 'auditoria',
                'verbose_name_plural': 'auditorias',
                'db_table': 'AUDITORIA',
            },
        ),
        migrations.CreateModel(
            name='EMPLEADO',
            fields=[
                ('codigo_emp', models.AutoField(primary_key=True, serialize=False)),
                ('rut_emp', models.CharField(max_length=10, verbose_name='rut empleado (sin puntos con guion)')),
                ('nom_emp', models.CharField(max_length=30, verbose_name='nombre')),
                ('appaterno_emp', models.CharField(max_length=30, verbose_name='apellido paterno')),
                ('apmaterno_emp', models.CharField(max_length=30, verbose_name='apellido materno')),
                ('clave', models.CharField(max_length=50, verbose_name='contraseña')),
            ],
            options={
                'verbose_name': 'empleado',
                'verbose_name_plural': 'empleados',
                'db_table': 'EMPLEADO',
            },
        ),
        migrations.CreateModel(
            name='EMPRESA',
            fields=[
                ('id_empresa', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_empresa', models.CharField(max_length=30, verbose_name='nombre empresa')),
            ],
            options={
                'verbose_name': 'empresa',
                'verbose_name_plural': 'empresas',
                'db_table': 'EMPRESA',
            },
        ),
        migrations.CreateModel(
            name='ERRORES',
            fields=[
                ('correlativo_error', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_error', models.DateField(auto_now_add=True, verbose_name='fecha error')),
                ('nombre_modulo', models.CharField(max_length=150, verbose_name='nombre modulo')),
                ('descripcion_error', models.CharField(max_length=200, verbose_name='descripcion error')),
            ],
            options={
                'verbose_name': 'error',
                'verbose_name_plural': 'errores',
                'db_table': 'ERRORES',
            },
        ),
        migrations.CreateModel(
            name='FORMA_PAGO',
            fields=[
                ('id_forma_pago', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_forma_pago', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'forma de pago',
                'verbose_name_plural': 'formas de pago',
                'db_table': 'FORMAS_PAGO',
            },
        ),
        migrations.CreateModel(
            name='INFORME_TICKET',
            fields=[
                ('correlativo_inf', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_informe', models.DateField(auto_now_add=True, verbose_name='fecha informe')),
                ('cant_boletas', models.PositiveIntegerField(verbose_name='cantidad de boletas')),
                ('cant_tickets', models.PositiveIntegerField(verbose_name='cantidad de tickets')),
                ('total_ventas', models.PositiveIntegerField(verbose_name='total de ventas')),
            ],
            options={
                'verbose_name': 'informe ticket',
                'verbose_name_plural': 'informes tickets',
                'db_table': 'INFORME_TICKET',
            },
        ),
        migrations.CreateModel(
            name='PERFIL',
            fields=[
                ('id_perfil', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_prefil', models.CharField(max_length=30, verbose_name='nombre prefil')),
                ('ticket_diario', models.PositiveIntegerField(default=1, verbose_name='cantidad de tickets diarios')),
                ('valor', models.PositiveIntegerField(verbose_name='valor ticket')),
                ('bonificacion', models.PositiveIntegerField(default=0, verbose_name='bonificacion')),
                ('saldo', models.IntegerField(verbose_name='Saldo disponible')),
            ],
            options={
                'verbose_name': 'perfil',
                'verbose_name_plural': 'perfiles',
                'db_table': 'PERFIL',
            },
        ),
        migrations.CreateModel(
            name='SUCURSAL',
            fields=[
                ('id_sucursal', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_sucursal', models.CharField(max_length=50, verbose_name='nombre sucursal')),
                ('direccion_sucursal', models.CharField(max_length=150, verbose_name='direccion sucursal')),
            ],
            options={
                'verbose_name': 'sucursal',
                'verbose_name_plural': 'sucursales',
                'db_table': 'SUCURSAL',
            },
        ),
        migrations.CreateModel(
            name='TIPO_PRODUCTO',
            fields=[
                ('id_tipo_producto', models.AutoField(primary_key=True, serialize=False)),
                ('nom_tipo_producto', models.CharField(max_length=30, verbose_name='nombre categoria')),
            ],
            options={
                'verbose_name': 'tipo producto',
                'verbose_name_plural': 'tipo productos',
                'db_table': 'TIPO_PRODUCTO',
            },
        ),
        migrations.CreateModel(
            name='TIPO_TICKET',
            fields=[
                ('id_tipo_ticket', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=30, verbose_name='tipo ticket')),
            ],
            options={
                'verbose_name': 'tipo de ticket',
                'verbose_name_plural': 'tipos de tickets',
                'db_table': 'TIPO_TICKET',
            },
        ),
        migrations.CreateModel(
            name='TURNO',
            fields=[
                ('id_turno', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30, verbose_name='nombre turno')),
                ('hora_inicio', models.CharField(max_length=5, verbose_name='hora inicio')),
                ('hora_termino', models.CharField(max_length=5, verbose_name='hora termino')),
            ],
            options={
                'verbose_name': 'turno',
                'verbose_name_plural': 'turnos',
                'db_table': 'TURNO',
            },
        ),
        migrations.CreateModel(
            name='TICKET',
            fields=[
                ('codigo_ticket', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_imp', models.DateField(auto_now_add=True, verbose_name='fecha impresion')),
                ('hora_vig_inicio', models.CharField(max_length=5, verbose_name='hora inicio')),
                ('hora_vig_termino', models.CharField(max_length=5, verbose_name='hora termino')),
                ('estado', models.BooleanField(default=True, verbose_name='estado del ticket')),
                ('valor', models.PositiveIntegerField(verbose_name='valor ticket')),
                ('comentario', models.TextField(blank=True, max_length=100, null=True, verbose_name='comentario')),
                ('fk_rut_emp', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CORE.empleado')),
                ('fk_tipo_ticket', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CORE.tipo_ticket')),
            ],
            options={
                'verbose_name': 'ticket',
                'verbose_name_plural': 'tickets',
                'db_table': 'TICKET',
            },
        ),
        migrations.CreateModel(
            name='PRODUCTO',
            fields=[
                ('codigo_producto', models.AutoField(primary_key=True, serialize=False)),
                ('nom_producto', models.CharField(max_length=30, verbose_name='nombre producto')),
                ('descripcion', models.TextField(max_length=100, verbose_name='descripcion')),
                ('precio', models.PositiveIntegerField(verbose_name='precio $')),
                ('fk_tipo_producto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CORE.tipo_producto')),
            ],
            options={
                'verbose_name': 'producto',
                'verbose_name_plural': 'productos',
                'db_table': 'PRODUCTO',
            },
        ),
        migrations.AddField(
            model_name='empleado',
            name='fk_empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CORE.empresa'),
        ),
        migrations.AddField(
            model_name='empleado',
            name='fk_perfil',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CORE.perfil'),
        ),
        migrations.AddField(
            model_name='empleado',
            name='fk_turno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CORE.turno'),
        ),
        migrations.CreateModel(
            name='DETALLE_TICKET',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(verbose_name='cantidad')),
                ('fk_codigo_producto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CORE.producto')),
                ('fk_num_ticket', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CORE.ticket')),
            ],
            options={
                'verbose_name': 'detalle ticket',
                'verbose_name_plural': 'detalle tickets',
                'db_table': 'DETALLE_TICKET',
            },
        ),
        migrations.CreateModel(
            name='DETALLE_AUDITORIA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_no_uso', models.DateField(verbose_name='fecha no uso')),
                ('fk_correlativo_aud', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CORE.auditoria')),
                ('fk_rut_emp', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CORE.empleado')),
            ],
            options={
                'verbose_name': 'detalle auditoria',
                'verbose_name_plural': 'detalle auditorias',
                'db_table': 'DETALLE_AUDITORIA',
            },
        ),
        migrations.CreateModel(
            name='CAJERO',
            fields=[
                ('rut_cajero', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='rut cajero')),
                ('nombre', models.CharField(max_length=30, verbose_name='nombre cajero')),
                ('clave', models.CharField(max_length=50, verbose_name='contraseña')),
                ('estado', models.BooleanField(default=False, verbose_name='habilitado')),
                ('administrador', models.BooleanField(default=False, verbose_name='Administrador')),
                ('fk_sucursal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CORE.sucursal')),
            ],
            options={
                'verbose_name': 'cajero',
                'verbose_name_plural': 'cajeros',
                'db_table': 'CAJERO',
            },
        ),
        migrations.CreateModel(
            name='BOLETA',
            fields=[
                ('num_boleta', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_boleta', models.DateField(auto_now_add=True, verbose_name='fecha emision')),
                ('valor_total', models.PositiveIntegerField(verbose_name='total')),
                ('valor_ticket', models.PositiveIntegerField(verbose_name='valor ticket')),
                ('saldo_por_pagar', models.PositiveIntegerField(default=0, null=True, verbose_name='saldo por pagar')),
                ('fk_codigo_ticket', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CORE.ticket')),
                ('fk_forma_pago', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CORE.forma_pago')),
                ('fk_rut_cajero', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CORE.cajero')),
            ],
            options={
                'verbose_name': 'boleta',
                'verbose_name_plural': 'boletas',
                'db_table': 'BOLETA',
            },
        ),
    ]
