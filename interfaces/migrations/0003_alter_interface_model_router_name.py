# Generated by Django 4.0.7 on 2023-07-16 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('interfaces', '0002_alter_interface_config_model_router_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interface_model',
            name='Router_Name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interfaces', to='interfaces.router_model'),
        ),
    ]
