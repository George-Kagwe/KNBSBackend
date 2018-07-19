# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-08 07:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0012_early_childhood_mortality_rates_by_sex'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fertility_By_Education_Status',
            fields=[
                ('fertility_id', models.AutoField(primary_key=True, serialize=False)),
                ('fertility', models.DecimalField(decimal_places=1, max_digits=10)),
                ('education_status', models.CharField(max_length=20)),
                ('year', models.CharField(max_length=10)),
            ],
        ),
    ]