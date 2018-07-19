# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-08 07:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0014_fertility_rate_by_age_and_residence'),
    ]

    operations = [
        migrations.CreateModel(
            name='Percentage_Adults_Who_Are_Current_Users',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('age_group', models.CharField(max_length=10)),
                ('women', models.DecimalField(decimal_places=1, max_digits=10)),
                ('men', models.DecimalField(decimal_places=1, max_digits=10)),
                ('category', models.CharField(max_length=10)),
            ],
        ),
    ]
