# Generated by Django 3.1.2 on 2021-04-11 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CORE', '0011_auto_20210411_0258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='des_prod',
            field=models.TextField(max_length=50, null=True, verbose_name='Descripcion'),
        ),
    ]
