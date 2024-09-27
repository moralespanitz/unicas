# Generated by Django 5.1.1 on 2024-09-16 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prestamos', '0005_prestamo_cuota'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamo',
            name='cuota',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='remaining_amount',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='remaining_installments',
            field=models.IntegerField(null=True),
        ),
    ]
