# Generated by Django 5.1.1 on 2024-09-19 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multas', '0004_alter_multa_reason'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multa',
            name='status',
            field=models.CharField(choices=[('PENDIENTE', 'Pendiente'), ('CANCELADO', 'Cancelado')], default='Pendiente', max_length=20),
        ),
    ]
