# Generated by Django 4.0.4 on 2022-05-11 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_cliente_rename_productos_producto_delete_clientes'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagenProducto',
            field=models.ImageField(null=True, upload_to='productos'),
        ),
    ]
