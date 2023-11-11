# Generated by Django 4.2.7 on 2023-11-11 17:54

import DistribuidoraCarne.validaciones
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DistribuidoraCarne', '0003_impuesto_valor_impuesto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encabezadofactura',
            name='nombre_negocio',
            field=models.CharField(max_length=200, validators=[DistribuidoraCarne.validaciones.validar_nombre_negocio]),
        ),
        migrations.AlterField(
            model_name='metodopago',
            name='numero_tarjeta',
            field=models.CharField(max_length=25, validators=[DistribuidoraCarne.validaciones.validar_numero_tarjeta]),
        ),
        migrations.AlterField(
            model_name='metodopago',
            name='tipo_metodo_pago',
            field=models.CharField(choices=[('debito', 'Débito'), ('credito', 'Crédito')], max_length=50, validators=[DistribuidoraCarne.validaciones.validar_descripcion]),
        ),
    ]
