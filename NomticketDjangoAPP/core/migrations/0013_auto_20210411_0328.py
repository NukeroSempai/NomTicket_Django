# Generated by Django 3.1.2 on 2021-04-11 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CORE', '0012_auto_20210411_0308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casino',
            name='dir_casino',
            field=models.CharField(max_length=50, verbose_name='Direccion Casino'),
        ),
        migrations.AlterField(
            model_name='casino',
            name='rsocial_casino',
            field=models.CharField(max_length=50, verbose_name='Razon Social Casino'),
        ),
        migrations.AlterField(
            model_name='casino',
            name='rut_casino',
            field=models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='Rut Casino'),
        ),
        migrations.AlterField(
            model_name='comedor',
            name='nom_comedor',
            field=models.CharField(max_length=30, verbose_name='Nombre Comedor'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='direccion_empresa',
            field=models.CharField(max_length=50, null=True, verbose_name='Direccion Empresa'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='rsocial_empresa',
            field=models.CharField(max_length=50, verbose_name='Razon Social Empresa'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='rut_empresa',
            field=models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='Rut Empresa'),
        ),
        migrations.AlterField(
            model_name='informe_ticket_mensual',
            name='comedor',
            field=models.CharField(max_length=30, verbose_name='Comedor'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nom_prod',
            field=models.CharField(max_length=30, verbose_name='Nombre Producto'),
        ),
        migrations.AlterField(
            model_name='sucursal',
            name='nom_sucursal',
            field=models.CharField(max_length=30, verbose_name='Nombre Sucursal'),
        ),
        migrations.AlterField(
            model_name='tipo_usuario',
            name='desc_tipo_usuario',
            field=models.CharField(max_length=30, verbose_name='Descripcion'),
        ),
    ]
