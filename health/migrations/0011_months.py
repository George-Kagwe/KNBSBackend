# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-28 07:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0010_sectors'),
    ]

    operations = [
        migrations.CreateModel(
            name='Months',
            fields=[
                ('month_id', models.AutoField(primary_key=True, serialize=False)),
                ('month', models.CharField(max_length=100)),
            ],
        ),
    ]
