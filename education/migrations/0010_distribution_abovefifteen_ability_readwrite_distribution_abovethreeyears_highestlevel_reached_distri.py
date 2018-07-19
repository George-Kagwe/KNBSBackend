# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-07-12 08:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0019_prevalence_of_overweight_and_obesity'),
        ('education', '0009_public_primaryteachers_trainingcollege_enrolment_public_secondary_school_teachers_by_sex_secondary_s'),
    ]

    operations = [
        migrations.CreateModel(
            name='Distribution_AboveFifteen_Ability_ReadWrite',
            fields=[
                ('distribution_id', models.AutoField(primary_key=True, serialize=False)),
                ('literate', models.DecimalField(decimal_places=1, max_digits=10)),
                ('illiterate', models.DecimalField(decimal_places=1, max_digits=10)),
                ('not_stated', models.DecimalField(decimal_places=1, max_digits=10)),
                ('no_of_individuals', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.Counties')),
            ],
        ),
        migrations.CreateModel(
            name='Distribution_AboveThreeYears_Highestlevel_Reached',
            fields=[
                ('distribution_id', models.AutoField(primary_key=True, serialize=False)),
                ('pre_primary', models.DecimalField(decimal_places=1, max_digits=10)),
                ('primary', models.DecimalField(decimal_places=1, max_digits=10)),
                ('post_primary', models.DecimalField(decimal_places=1, max_digits=10)),
                ('secondary', models.DecimalField(decimal_places=1, max_digits=10)),
                ('college', models.DecimalField(decimal_places=1, max_digits=10)),
                ('university', models.DecimalField(decimal_places=1, max_digits=10)),
                ('madrassa_duksi', models.DecimalField(decimal_places=1, max_digits=10)),
                ('other', models.DecimalField(decimal_places=1, max_digits=10)),
                ('not_stated', models.DecimalField(decimal_places=1, max_digits=10)),
                ('no_of_individuals', models.IntegerField()),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.Counties')),
            ],
        ),
        migrations.CreateModel(
            name='Distribution_AboveThreeYears_Training',
            fields=[
                ('distribution_id', models.AutoField(primary_key=True, serialize=False)),
                ('ever_attended', models.DecimalField(decimal_places=1, max_digits=10)),
                ('never_attended', models.DecimalField(decimal_places=1, max_digits=10)),
                ('not_stated', models.DecimalField(decimal_places=1, max_digits=10)),
                ('no_of_individuals', models.IntegerField()),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.Counties')),
            ],
        ),
        migrations.CreateModel(
            name='Distribution_Highest_Education_Qualification',
            fields=[
                ('distribution_id', models.AutoField(primary_key=True, serialize=False)),
                ('none', models.DecimalField(decimal_places=1, max_digits=10)),
                ('cpe_kcpe', models.DecimalField(decimal_places=1, max_digits=10)),
                ('kape', models.DecimalField(decimal_places=1, max_digits=10)),
                ('kjse', models.DecimalField(decimal_places=1, max_digits=10)),
                ('kce_kcse', models.DecimalField(decimal_places=1, max_digits=10)),
                ('kace_eaace', models.DecimalField(decimal_places=1, max_digits=10)),
                ('certificate', models.DecimalField(decimal_places=1, max_digits=10)),
                ('diploma', models.DecimalField(decimal_places=1, max_digits=10)),
                ('degree', models.DecimalField(decimal_places=1, max_digits=10)),
                ('post_literacy_cert', models.DecimalField(decimal_places=1, max_digits=10)),
                ('other', models.DecimalField(decimal_places=1, max_digits=10)),
                ('not_stated', models.DecimalField(decimal_places=1, max_digits=10)),
                ('no_of_individuals', models.IntegerField()),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.Counties')),
            ],
        ),
        migrations.CreateModel(
            name='Distribution_SixThirteen_By_SchoolType',
            fields=[
                ('distribution_id', models.AutoField(primary_key=True, serialize=False)),
                ('day', models.DecimalField(decimal_places=1, max_digits=10)),
                ('boarding', models.DecimalField(decimal_places=1, max_digits=10)),
                ('not_stated', models.DecimalField(decimal_places=1, max_digits=10)),
                ('type', models.CharField(max_length=10)),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.Counties')),
            ],
        ),
        migrations.CreateModel(
            name='Distribution_Three_Twentyfour_SchoolAttendance',
            fields=[
                ('distribution_id', models.AutoField(primary_key=True, serialize=False)),
                ('currently_attending', models.DecimalField(decimal_places=1, max_digits=10)),
                ('not_attending', models.DecimalField(decimal_places=1, max_digits=10)),
                ('no_of_individuals', models.IntegerField()),
                ('age_group', models.CharField(max_length=10)),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.Counties')),
            ],
        ),
        migrations.CreateModel(
            name='Gross_Attendance_Ratio_By_Level',
            fields=[
                ('ratio_id', models.AutoField(primary_key=True, serialize=False)),
                ('pre_primary', models.DecimalField(decimal_places=1, max_digits=10)),
                ('primary', models.DecimalField(decimal_places=1, max_digits=10)),
                ('secondary', models.DecimalField(decimal_places=1, max_digits=10)),
                ('gender', models.CharField(max_length=10)),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.Counties')),
            ],
        ),
        migrations.CreateModel(
            name='Net_Attendance_Ratio_By_Level',
            fields=[
                ('ratio_id', models.AutoField(primary_key=True, serialize=False)),
                ('pre_primary', models.DecimalField(decimal_places=1, max_digits=10)),
                ('primary', models.DecimalField(decimal_places=1, max_digits=10)),
                ('secondary', models.DecimalField(decimal_places=1, max_digits=10)),
                ('gender', models.CharField(max_length=10)),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.Counties')),
            ],
        ),
        migrations.CreateModel(
            name='Population_Distribution_Above_Three_School_Attendance',
            fields=[
                ('distribution_id', models.AutoField(primary_key=True, serialize=False)),
                ('currently_attending', models.DecimalField(decimal_places=1, max_digits=10)),
                ('not_attending', models.DecimalField(decimal_places=1, max_digits=10)),
                ('no_of_individuals', models.IntegerField()),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.Counties')),
            ],
        ),
    ]