# Generated by Django 3.0.14 on 2023-08-09 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20230809_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='menu_item',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='reciperequirements',
            name='menu_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.MenuItem'),
        ),
    ]
