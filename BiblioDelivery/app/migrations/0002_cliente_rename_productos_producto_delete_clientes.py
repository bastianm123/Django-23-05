# Generated by Django 4.0.4 on 2022-05-11 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('rutCliente', models.IntegerField(max_length=9, primary_key=True, serialize=False, verbose_name='Rut cliente')),
                ('nombreCliente', models.CharField(max_length=20, verbose_name='Nombre Cliente')),
                ('direccionCliente', models.CharField(max_length=20, verbose_name='Direccion Cliente')),
                ('numeroCliente', models.IntegerField(max_length=9, verbose_name='Numero Cliente')),
                ('emailCliente', models.EmailField(max_length=254, verbose_name='Correo Cliente')),
                ('fechanacimientoCliente', models.DateField(verbose_name='Fecha Nacimiento Cliente')),
            ],
        ),
        migrations.RenameModel(
            old_name='Productos',
            new_name='Producto',
        ),
        migrations.DeleteModel(
            name='Clientes',
        ),
    ]
