# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-19 07:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade_and_commerce', '0003_balance_of_trade_import_trade_africa_countries_quantities_principal_domestic_exports_quantities_prin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Value_Of_Total_Exports_All_Destinations',
            fields=[
                ('export_id', models.AutoField(primary_key=True, serialize=False)),
                ('region', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('value_in_millions', models.DecimalField(decimal_places=2, max_digits=65)),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Value_of_Total_Exports_European_Union',
            fields=[
                ('export_id', models.AutoField(primary_key=True, serialize=False)),
                ('country', models.CharField(max_length=100)),
                ('value_in_millions', models.DecimalField(decimal_places=2, max_digits=65)),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Value_Total_Exports_East_Africa_Communities',
            fields=[
                ('export_id', models.AutoField(primary_key=True, serialize=False)),
                ('country', models.CharField(max_length=100)),
                ('value_in_millions', models.DecimalField(decimal_places=2, max_digits=65)),
                ('year', models.IntegerField()),
            ],
        ),
    ]
