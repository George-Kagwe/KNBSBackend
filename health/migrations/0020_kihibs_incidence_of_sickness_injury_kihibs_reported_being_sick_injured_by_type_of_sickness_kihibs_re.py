# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-07-17 07:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0019_prevalence_of_overweight_and_obesity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kihibs_Incidence_Of_Sickness_Injury',
            fields=[
                ('distribution_id', models.AutoField(primary_key=True, serialize=False)),
                ('sick_injured', models.DecimalField(decimal_places=1, max_digits=10)),
                ('no_of_individuals', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.Counties')),
            ],
        ),
        migrations.CreateModel(
            name='Kihibs_Reported_Being_Sick_Injured_By_Type_Of_Sickness',
            fields=[
                ('distribution_id', models.AutoField(primary_key=True, serialize=False)),
                ('fever_malaria', models.DecimalField(decimal_places=1, max_digits=10)),
                ('stomach_problems', models.DecimalField(decimal_places=1, max_digits=10)),
                ('diarrhoea', models.DecimalField(decimal_places=1, max_digits=10)),
                ('vomiting', models.DecimalField(decimal_places=1, max_digits=10)),
                ('upper_respiratory_infection', models.DecimalField(decimal_places=1, max_digits=10)),
                ('lower_respiratory_infection', models.DecimalField(decimal_places=1, max_digits=10)),
                ('flu', models.DecimalField(decimal_places=1, max_digits=10)),
                ('asthma', models.DecimalField(decimal_places=1, max_digits=10)),
                ('headache', models.DecimalField(decimal_places=1, max_digits=10)),
                ('skin_problem', models.DecimalField(decimal_places=1, max_digits=10)),
                ('dental_problem', models.DecimalField(decimal_places=1, max_digits=10)),
                ('eye_problem', models.DecimalField(decimal_places=1, max_digits=10)),
                ('ear_nose_throat', models.DecimalField(decimal_places=1, max_digits=10)),
                ('backache', models.DecimalField(decimal_places=1, max_digits=10)),
                ('tb', models.DecimalField(decimal_places=1, max_digits=10)),
                ('heart_problem', models.DecimalField(decimal_places=1, max_digits=10)),
                ('blood_pressure', models.DecimalField(decimal_places=1, max_digits=10)),
                ('pain_while_passing_urine', models.DecimalField(decimal_places=1, max_digits=10)),
                ('diabetes', models.DecimalField(decimal_places=1, max_digits=10)),
                ('mental_disorder', models.DecimalField(decimal_places=1, max_digits=10)),
                ('stis', models.DecimalField(decimal_places=1, max_digits=10)),
                ('burn', models.DecimalField(decimal_places=1, max_digits=10)),
                ('fracture', models.DecimalField(decimal_places=1, max_digits=10)),
                ('wound_cut', models.DecimalField(decimal_places=1, max_digits=10)),
                ('poisoning', models.DecimalField(decimal_places=1, max_digits=10)),
                ('pregnancy_related', models.DecimalField(decimal_places=1, max_digits=10)),
                ('cancer', models.DecimalField(decimal_places=1, max_digits=10)),
                ('other_long_term_illness', models.DecimalField(decimal_places=1, max_digits=10)),
                ('hiv_aids', models.DecimalField(decimal_places=1, max_digits=10)),
                ('typhoid', models.DecimalField(decimal_places=1, max_digits=10)),
                ('other', models.DecimalField(decimal_places=1, max_digits=10)),
                ('no_of_individuals', models.IntegerField()),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.Counties')),
            ],
        ),
        migrations.CreateModel(
            name='Kihibs_Reported_Sickness_By_Age_Group',
            fields=[
                ('distribution_id', models.AutoField(primary_key=True, serialize=False)),
                ('percentage_distribution', models.DecimalField(decimal_places=1, max_digits=10)),
                ('age_group', models.CharField(max_length=10)),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.Counties')),
            ],
        ),
    ]
