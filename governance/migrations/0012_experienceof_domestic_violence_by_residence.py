# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-30 07:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('governance', '0011_experienceof_domestic_violence_by_marital_success'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experienceof_Domestic_Violence_By_Residence',
            fields=[
                ('woman_id', models.AutoField(primary_key=True, serialize=False)),
                ('residence', models.CharField(max_length=10)),
                ('percentage_experienced_physical_violence', models.DecimalField(decimal_places=1, max_digits=10)),
                ('percentage_experienced_sexual_violence', models.DecimalField(decimal_places=1, max_digits=10)),
                ('percentage_experienced_physical_and_sexual_violence', models.DecimalField(decimal_places=1, max_digits=10)),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
    ]
