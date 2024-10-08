# Generated by Django 5.1.1 on 2024-09-22 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prestamos', '0011_alter_prestamo_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prestamo',
            name='cuota',
        ),
        migrations.AddField(
            model_name='prestamo',
            name='loan_type',
            field=models.CharField(choices=[('Cuota a rebatir', 'Cuota Rebatir'), ('Cuota fija', 'Cuota Fija'), ('Cuota a vencimiento', 'Cuota Vencimiento'), ('Cuota variable', 'Cuota Variable')], default='Cuota fija', max_length=20),
        ),
    ]
