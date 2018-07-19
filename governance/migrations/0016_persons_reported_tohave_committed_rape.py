# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-30 07:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('governance', '0015_persons_reported_tohave_committed_defilement'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persons_Reported_ToHave_Committed_Rape',
            fields=[
                ('persons_id', models.AutoField(primary_key=True, serialize=False)),
                ('number', models.IntegerField()),
                ('proportion', models.DecimalField(decimal_places=1, max_digits=10)),
                ('gender', models.CharField(max_length=20)),
                ('year', models.IntegerField()),
            ],
        ),
    ]