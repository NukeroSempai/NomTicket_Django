# Generated by Django 3.1.2 on 2021-04-24 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CORE', '0002_auto_20210424_1241'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detalle_auditoria',
            old_name='fk_rut_emp',
            new_name='fk_codigo_emp',
        ),
        migrations.RenameField(
            model_name='ticket',
            old_name='fk_rut_emp',
            new_name='fk_codigo_emp',
        ),
    ]