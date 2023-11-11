# Generated by Django 4.2.7 on 2023-11-11 17:14

import DistribuidoraCarne.validaciones
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DistribuidoraCarne', '0002_encabezadofactura_impuesto_metodopago'),
    ]

    operations = [
        migrations.AddField(
            model_name='impuesto',
            name='valor_impuesto',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5, validators=[DistribuidoraCarne.validaciones.validar_valor_impuesto]),
        ),
        migrations.AlterField(
            model_name='encabezadofactura',
            name='correo',
            field=models.CharField(max_length=100, null=True, validators=[DistribuidoraCarne.validaciones.validar_correo]),
        ),
        migrations.AlterField(
            model_name='encabezadofactura',
            name='direccion_negocio',
            field=models.CharField(max_length=200, validators=[DistribuidoraCarne.validaciones.validar_direccion]),
        ),
        migrations.AlterField(
            model_name='encabezadofactura',
            name='nombre_negocio',
            field=models.CharField(max_length=200, validators=[DistribuidoraCarne.validaciones.validar_nombre]),
        ),
        migrations.AlterField(
            model_name='encabezadofactura',
            name='rtn',
            field=models.CharField(max_length=20, validators=[DistribuidoraCarne.validaciones.validar_rtn]),
        ),
        migrations.AlterField(
            model_name='encabezadofactura',
            name='telefono',
            field=models.CharField(max_length=20, null=True, validators=[DistribuidoraCarne.validaciones.validar_telefono]),
        ),
        migrations.AlterField(
            model_name='impuesto',
            name='nombre_impuesto',
            field=models.CharField(max_length=20, validators=[DistribuidoraCarne.validaciones.validar_nombre]),
        ),
        migrations.AlterField(
            model_name='impuesto',
            name='tipo_impuesto',
            field=models.CharField(max_length=50, validators=[DistribuidoraCarne.validaciones.validar_descripcion]),
        ),
        migrations.AlterField(
            model_name='metodopago',
            name='cvv',
            field=models.CharField(max_length=4, validators=[DistribuidoraCarne.validaciones.validar_cvv]),
        ),
        migrations.AlterField(
            model_name='metodopago',
            name='fecha_vencimiento',
            field=models.DateField(validators=[DistribuidoraCarne.validaciones.validar_fecha_vencimiento]),
        ),
        migrations.AlterField(
            model_name='metodopago',
            name='nombre_metodo_pago',
            field=models.CharField(max_length=50, validators=[DistribuidoraCarne.validaciones.validar_nombre]),
        ),
        migrations.AlterField(
            model_name='metodopago',
            name='nombre_titular',
            field=models.CharField(max_length=60, validators=[DistribuidoraCarne.validaciones.validar_nombre_titular]),
        ),
        migrations.AlterField(
            model_name='metodopago',
            name='numero_tarjeta',
            field=models.CharField(max_length=16, validators=[DistribuidoraCarne.validaciones.validar_numero_tarjeta]),
        ),
        migrations.AlterField(
            model_name='metodopago',
            name='tipo_metodo_pago',
            field=models.CharField(max_length=50, validators=[DistribuidoraCarne.validaciones.validar_descripcion]),
        ),
    ]
