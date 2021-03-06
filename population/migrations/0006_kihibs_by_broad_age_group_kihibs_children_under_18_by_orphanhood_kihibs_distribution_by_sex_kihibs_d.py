# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-07-31 15:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0023_sectors'),
        ('population', '0005_distribution_sex_number_households_area_density'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kihibs_By_Broad_Age_Group',
            fields=[
                ('group_id', models.AutoField(primary_key=True, serialize=False)),
                ('range_0_14', models.DecimalField(decimal_places=1, max_digits=10)),
                ('range_15_64', models.DecimalField(decimal_places=1, max_digits=10)),
                ('over_65', models.DecimalField(decimal_places=1, max_digits=10)),
                ('not_stated', models.DecimalField(decimal_places=1, max_digits=10)),
                ('age_depend_ratio', models.DecimalField(decimal_places=1, max_digits=10)),
                ('child_depend_ratio', models.DecimalField(decimal_places=1, max_digits=10)),
                ('old_age_depend_ratio', models.DecimalField(decimal_places=1, max_digits=10)),
                ('individuals', models.IntegerField()),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.Counties')),
            ],
        ),
        migrations.CreateModel(
            name='Kihibs_Children_Under_18_By_Orphanhood',
            fields=[
                ('distribution_id', models.AutoField(primary_key=True, serialize=False)),
                ('living_with_both', models.DecimalField(decimal_places=1, max_digits=10)),
                ('father_alive', models.DecimalField(decimal_places=1, max_digits=10)),
                ('father_deceased', models.DecimalField(decimal_places=1, max_digits=10)),
                ('mother_alive', models.DecimalField(decimal_places=1, max_digits=10)),
                ('mother_deceased', models.DecimalField(decimal_places=1, max_digits=10)),
                ('both_alive', models.DecimalField(decimal_places=1, max_digits=10)),
                ('only_father_alive', models.DecimalField(decimal_places=1, max_digits=10)),
                ('only_mother_alive', models.DecimalField(decimal_places=1, max_digits=10)),
                ('both_parents_deceased', models.DecimalField(decimal_places=1, max_digits=10)),
                ('missing_info', models.DecimalField(decimal_places=1, max_digits=10)),
                ('orphanhood', models.DecimalField(decimal_places=1, max_digits=10)),
                ('individuals', models.IntegerField()),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.Counties')),
            ],
        ),
        migrations.CreateModel(
            name='Kihibs_Distribution_By_Sex',
            fields=[
                ('distribution_id', models.AutoField(primary_key=True, serialize=False)),
                ('male_individuals', models.IntegerField()),
                ('male_per_cent', models.DecimalField(decimal_places=1, max_digits=10)),
                ('female_individuals', models.IntegerField()),
                ('female_per_cent', models.DecimalField(decimal_places=1, max_digits=10)),
                ('sex_ratio', models.DecimalField(decimal_places=1, max_digits=10)),
                ('individuals', models.IntegerField()),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.Counties')),
            ],
        ),
        migrations.CreateModel(
            name='Kihibs_Distribution_Of_Households_By_Size',
            fields=[
                ('distribution_id', models.AutoField(primary_key=True, serialize=False)),
                ('range_1_2_persons', models.DecimalField(decimal_places=1, max_digits=10)),
                ('range_3_4_persons', models.DecimalField(decimal_places=1, max_digits=10)),
                ('range_5_6_persons', models.DecimalField(decimal_places=1, max_digits=10)),
                ('over_7_persons', models.DecimalField(decimal_places=1, max_digits=10)),
                ('households', models.IntegerField()),
                ('mean_hhold_size', models.DecimalField(decimal_places=1, max_digits=10)),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.Counties')),
            ],
        ),
        migrations.CreateModel(
            name='Kihibs_Hholds_By_Sex_Of_Household_Head',
            fields=[
                ('head_id', models.AutoField(primary_key=True, serialize=False)),
                ('male', models.DecimalField(decimal_places=1, max_digits=10)),
                ('female', models.DecimalField(decimal_places=1, max_digits=10)),
                ('households', models.IntegerField()),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.Counties')),
            ],
        ),
        migrations.CreateModel(
            name='Kihibs_Marital_Status_Above_18_Years',
            fields=[
                ('status_id', models.AutoField(primary_key=True, serialize=False)),
                ('monogamous', models.DecimalField(decimal_places=1, max_digits=10)),
                ('polygamous', models.DecimalField(decimal_places=1, max_digits=10)),
                ('living_together', models.DecimalField(decimal_places=1, max_digits=10)),
                ('seperated', models.DecimalField(decimal_places=1, max_digits=10)),
                ('divorced', models.DecimalField(decimal_places=1, max_digits=10)),
                ('widow_widower', models.DecimalField(decimal_places=1, max_digits=10)),
                ('never_married', models.DecimalField(decimal_places=1, max_digits=10)),
                ('individuals', models.IntegerField()),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.Counties')),
            ],
        ),
    ]
