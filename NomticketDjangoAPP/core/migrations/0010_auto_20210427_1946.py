# Generated by Django 3.1.2 on 2021-04-27 23:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CORE', '0009_auto_20210426_2351'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perfil',
            old_name='nombre_prefil',
            new_name='nombre_perfil',
        ),
    ]
