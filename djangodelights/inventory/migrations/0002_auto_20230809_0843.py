# Generated by Django 3.0.14 on 2023-08-09 06:43

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reciperequirements',
            name='measurement_unit',
        ),
        migrations.AddField(
            model_name='purchase',
            name='timestamp',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='menu_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.MenuItem'),
        ),
    ]
