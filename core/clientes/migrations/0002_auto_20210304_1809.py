# Generated by Django 3.1.4 on 2021-03-04 23:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pagosmensualidadesclientes',
            old_name='fecha',
            new_name='fecha_pago',
        ),
        migrations.AlterField(
            model_name='clientes',
            name='fecha_de_instalacion',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 4, 18, 9, 5, 951512)),
        ),
        migrations.AlterField(
            model_name='contratoclientes',
            name='fecha_contrato',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 4, 18, 9, 5, 951077)),
        ),
    ]
