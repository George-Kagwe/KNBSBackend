# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-03 12:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('population', '0003_by_sex_and_age_groups_by_sex_and_school_attendance_by_type_of_disability_distribution_sex_number_hou'),
    ]

    operations = [
        # migrations.CreateModel(
        #     name='Distribution_Sex_Number_Households_Area_Density',
        #     fields=[
        #         ('distribution_id', models.AutoField(primary_key=True, serialize=False)),
        #         ('area_in_square_km', models.DecimalField(decimal_places=2, max_digits=30)),
        #         ('county', models.CharField(max_length=100)),
        #         ('density', models.DecimalField(decimal_places=7, max_digits=30)),
        #         ('female', models.IntegerField()),
        #         ('male', models.IntegerField()),
        #         ('no_of_houseHolds', models.IntegerField()),
        #         ('total_population', models.IntegerField()),
        #     ],
        # ),
    ]