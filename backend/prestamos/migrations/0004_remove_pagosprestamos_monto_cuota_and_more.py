# Generated by Django 5.1.1 on 2024-09-16 23:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prestamos', '0003_pagosprestamos_member'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pagosprestamos',
            name='monto_cuota',
        ),
        migrations.RemoveField(
            model_name='pagosprestamos',
            name='monto_interes',
        ),
    ]
