# Generated by Django 4.2.6 on 2023-11-18 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Sucursal', '0001_initial'),
        ('Auto', '0005_sucursal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sucursal',
            name='sucursal',
        ),
        migrations.AddField(
            model_name='auto',
            name='sucursal',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='autos', to='Sucursal.sucursal'),
        ),
    ]
