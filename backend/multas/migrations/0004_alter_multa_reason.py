# Generated by Django 5.1.1 on 2024-09-19 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multas', '0003_alter_multa_junta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multa',
            name='reason',
            field=models.CharField(choices=[('TARDANZA', 'Tardanza'), ('INASISTENCIA', 'Inasistencia'), ('OTROS', 'Otros')], default='OTROS', max_length=255),
        ),
    ]
