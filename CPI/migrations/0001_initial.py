# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-12 15:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Annual_Avg_Retail_Prices_Of_Certain_Consumer_Goods_In_Kenya',
            fields=[
                ('avg_retail_price_id', models.AutoField(primary_key=True, serialize=False)),
                ('item', models.CharField(max_length=100)),
                ('unit', models.CharField(max_length=100)),
                ('ksh_per_unit', models.DecimalField(decimal_places=10, max_digits=20)),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Consumer_Price_Index',
            fields=[
                ('cpi_retail_price_id', models.AutoField(primary_key=True, serialize=False)),
                ('month', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('group', models.CharField(max_length=100)),
                ('food_and_non_alcoholic_beverages', models.DecimalField(decimal_places=10, max_digits=20)),
                ('alcoholic_beverages_tobacco_narcotics', models.DecimalField(decimal_places=10, max_digits=20)),
                ('clothing_and_footwear', models.DecimalField(decimal_places=10, max_digits=20)),
                ('housing_water_electricity_gas_and_other_fuels', models.DecimalField(decimal_places=10, max_digits=20)),
                ('furnishings_household_equipment_routine_household_maintenance', models.DecimalField(decimal_places=10, max_digits=20)),
                ('health', models.DecimalField(decimal_places=10, max_digits=20)),
                ('transport', models.DecimalField(decimal_places=10, max_digits=20)),
                ('communication', models.DecimalField(decimal_places=10, max_digits=20)),
                ('recreation_and_culture', models.DecimalField(decimal_places=10, max_digits=20)),
                ('education', models.DecimalField(decimal_places=10, max_digits=20)),
                ('restaurant_and_hotels', models.DecimalField(decimal_places=10, max_digits=20)),
                ('miscellaneous_goods_and_services', models.DecimalField(decimal_places=10, max_digits=20)),
                ('total', models.DecimalField(decimal_places=10, max_digits=20)),
            ],
        ),
        migrations.CreateModel(
            name='Elementary_Aggregates_Weights_In_The_Cpi_Baskets',
            fields=[
                ('aggregate_weights_id', models.AutoField(primary_key=True, serialize=False)),
                ('coicop_code', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('nairobi_lower', models.DecimalField(decimal_places=10, max_digits=20)),
                ('nairobi_middle', models.DecimalField(decimal_places=10, max_digits=20)),
                ('nairobi_upper', models.DecimalField(decimal_places=10, max_digits=20)),
                ('rest_of_urban_areas', models.DecimalField(decimal_places=10, max_digits=20)),
                ('kenya', models.DecimalField(decimal_places=10, max_digits=20)),
            ],
        ),
        migrations.CreateModel(
            name='Group_Weights_For_Kenya_Cpi_Febuary_Base_2009',
            fields=[
                ('group_weights_id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
                ('household', models.CharField(max_length=100)),
                ('group_weights', models.DecimalField(decimal_places=10, max_digits=20)),
            ],
        ),
        migrations.CreateModel(
            name='Group_Weights_For_Kenya_Cpi_October_Base_1997',
            fields=[
                ('group_weight_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_group', models.CharField(max_length=100)),
                ('household', models.CharField(max_length=100)),
                ('group_weights', models.DecimalField(decimal_places=10, max_digits=20)),
            ],
        ),
    ]