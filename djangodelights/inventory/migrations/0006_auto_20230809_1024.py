# Generated by Django 3.0.14 on 2023-08-09 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_auto_20230809_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reciperequirements',
            name='menu_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.MenuItem'),
        ),
    ]
