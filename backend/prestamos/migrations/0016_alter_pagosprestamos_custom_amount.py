# Generated by Django 5.1.1 on 2024-09-24 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prestamos', '0015_alter_pagosprestamos_fecha_pago'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagosprestamos',
            name='custom_amount',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
