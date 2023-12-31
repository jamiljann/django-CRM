# Generated by Django 4.0.7 on 2023-06-23 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('routers', '0003_routerconfig_model_ip_routerconfig_model_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Router_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Type', models.CharField(max_length=50)),
                ('IP', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Interface_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('int_Name', models.CharField(max_length=50)),
                ('Description', models.CharField(blank=True, max_length=155)),
                ('int_ID', models.CharField(blank=True, max_length=15)),
                ('IP', models.CharField(blank=True, max_length=35)),
                ('Profile', models.CharField(blank=True, max_length=25)),
                ('VPN', models.CharField(blank=True, max_length=50)),
                ('Encapsulation', models.CharField(blank=True, max_length=50)),
                ('Int_type', models.CharField(max_length=15)),
                ('Router_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='routers.routerconfig_model')),
            ],
        ),
        migrations.CreateModel(
            name='Interface_config_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('int_Conf', models.CharField(max_length=550)),
                ('Router_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Int_cross', to='routers.routerconfig_model')),
            ],
        ),
    ]
