# Generated by Django 4.2.3 on 2023-07-10 04:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core_mascotas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuentas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_cuenta', models.CharField(choices=[('Cliente', 'Cliente'), ('Administrador', 'Administrador'), ('Superusuario', 'Superusuario')], max_length=50, verbose_name='Tipo usuario')),
                ('rut', models.CharField(max_length=15, verbose_name='RUT')),
                ('direccion', models.CharField(max_length=400, verbose_name='Dirección')),
                ('subscrito', models.BooleanField(verbose_name='Subscrito')),
                ('imagen', models.ImageField(upload_to='perfiles/', verbose_name='Imagen')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Cuentas de usuario',
                'verbose_name_plural': 'Cuentas de usuarios',
                'db_table': 'Cuentas',
            },
        ),
    ]
