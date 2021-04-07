# Generated by Django 3.1.2 on 2021-04-07 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CORE', '0003_casino_comedor_producto_sucursal'),
    ]

    operations = [
        migrations.CreateModel(
            name='boleta',
            fields=[
                ('num_boleta', models.AutoField(primary_key=True, serialize=False)),
                ('fec_boleta', models.DateField(auto_now_add=True, verbose_name='fecha de boleta')),
                ('valor_total', models.IntegerField(verbose_name='Valor Total')),
                ('valor_ticket', models.IntegerField(null=True, verbose_name='Valor Ticket')),
                ('saldo_por_pagar', models.IntegerField(null=True, verbose_name='Saldo por Pagar')),
            ],
            options={
                'verbose_name': 'Boleta',
                'verbose_name_plural': 'Boletas',
            },
        ),
        migrations.CreateModel(
            name='categoria_empleado',
            fields=[
                ('id_categoria_emp', models.AutoField(primary_key=True, serialize=False)),
                ('desc_categoria_emp', models.CharField(max_length=30, verbose_name='Descripcion Categoria Empleado')),
            ],
            options={
                'verbose_name': 'Categoria Empleado',
                'verbose_name_plural': 'Categoriass de Empleados',
            },
        ),
        migrations.CreateModel(
            name='departamento',
            fields=[
                ('id_departamento', models.AutoField(primary_key=True, serialize=False)),
                ('nom_departamento', models.CharField(max_length=30, verbose_name='Nombre Departamento')),
            ],
            options={
                'verbose_name': 'Departamento',
                'verbose_name_plural': 'Departamentos',
            },
        ),
        migrations.CreateModel(
            name='error_calc_tickets',
            fields=[
                ('correl_error', models.AutoField(primary_key=True, serialize=False)),
                ('rutina_error', models.CharField(max_length=150, verbose_name='error en')),
                ('descrip_error', models.CharField(max_length=200, verbose_name='descripcion error')),
            ],
            options={
                'verbose_name': 'Error de calculo de ticket',
                'verbose_name_plural': 'Errores de calculo de tickets',
            },
        ),
        migrations.CreateModel(
            name='forma_pago',
            fields=[
                ('cod_forma_pago', models.AutoField(primary_key=True, serialize=False)),
                ('nom_forma_pago', models.CharField(max_length=30, verbose_name='Nombre forma de pago')),
            ],
            options={
                'verbose_name': 'Forma de pago',
                'verbose_name_plural': 'Formas de pago',
            },
        ),
        migrations.CreateModel(
            name='informe_ticket_mensual',
            fields=[
                ('correlativo_inf', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_proceso', models.DateField(auto_now_add=True, verbose_name='Fecha de proceso')),
                ('comedor', models.CharField(max_length=15, verbose_name='Comedor')),
                ('total_boletas', models.IntegerField(max_length=6)),
                ('total_tickets', models.IntegerField(max_length=9)),
                ('total_ventas', models.IntegerField(max_length=9)),
                ('cant_boletas', models.IntegerField(max_length=9)),
                ('cant_tickets', models.IntegerField(max_length=9)),
            ],
            options={
                'verbose_name': 'Informe',
                'verbose_name_plural': 'Informes',
            },
        ),
        migrations.CreateModel(
            name='pedido_casino',
            fields=[
                ('cod_pedido', models.AutoField(primary_key=True, serialize=False)),
                ('fec_pedido', models.DateField(auto_now_add=True, verbose_name='Fecha de pedido')),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
            },
        ),
        migrations.CreateModel(
            name='ticket',
            fields=[
                ('cod_ticket', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_imp', models.DateField(auto_now_add=True, verbose_name='Fecha de impresion')),
                ('hora_vig_inicio', models.CharField(max_length=5, verbose_name='vigencia Hora Inicio')),
                ('hora_vig_termino', models.CharField(max_length=5, verbose_name='vigencia Hora Termino')),
            ],
            options={
                'verbose_name': 'Ticket',
                'verbose_name_plural': 'Tickets',
            },
        ),
        migrations.CreateModel(
            name='tipo_usuario',
            fields=[
                ('cod_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('desc_tipo_usuario', models.CharField(max_length=15, verbose_name='Descripcion')),
            ],
            options={
                'verbose_name': 'Tipo de usuario',
                'verbose_name_plural': 'Tipos de usuarios',
            },
        ),
        migrations.CreateModel(
            name='turno',
            fields=[
                ('id_turno', models.AutoField(primary_key=True, serialize=False)),
                ('nom_turno', models.CharField(max_length=15, verbose_name='Nombre Turno')),
                ('hora_inicio', models.CharField(max_length=5, verbose_name='Hora inicio')),
                ('hora_termino', models.CharField(max_length=5, verbose_name='Hora termino')),
            ],
            options={
                'verbose_name': 'Turno',
                'verbose_name_plural': 'Turnos',
            },
        ),
    ]
