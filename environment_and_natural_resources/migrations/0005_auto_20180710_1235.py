# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-07-10 09:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('environment_and_natural_resources', '0004_development_expenditure_water_expenditure_cleaning_refuse_water_purification_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='average_export_prices_ash',
            name='year',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='development_expenditure_water',
            name='year',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='expenditure_cleaning_refuse',
            name='year',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='government_forest',
            name='year',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='num_high_risk_environ_impact',
            name='year',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='population_wildlife',
            name='year',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='quantity_of_total_mineral',
            name='year',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='quantity_value_fish_landed',
            name='year',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='record_sale_goverment_products',
            name='year',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='trends_envi_natural_resources',
            name='year',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='value_of_total_mineral',
            name='year',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='water_purification_points',
            name='year',
            field=models.IntegerField(),
        ),
    ]
