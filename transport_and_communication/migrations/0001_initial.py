# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-26 15:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('health', '0004_hospitalbedsandcots'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coverage_Of_Postal_Services',
            fields=[
                ('postal_coverage_id', models.AutoField(primary_key=True, serialize=False)),
                ('number', models.IntegerField()),
                ('year', models.IntegerField()),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.Counties')),
            ],
        ),
        migrations.CreateModel(
            name='Coverage_Of_Postal_Services_Ids',
            fields=[
                ('postal_service_id', models.AutoField(primary_key=True, serialize=False)),
                ('postal_service', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Coverage_Of_Telephone_Services',
            fields=[
                ('telephone_coverage_id', models.AutoField(primary_key=True, serialize=False)),
                ('number', models.IntegerField()),
                ('year', models.IntegerField()),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.Counties')),
            ],
        ),
        migrations.CreateModel(
            name='Coverage_Of_Telephone_Services_Ids',
            fields=[
                ('telephone_service_id', models.AutoField(primary_key=True, serialize=False)),
                ('telephone_service', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Road_Coverage_By_Type_And_Distance',
            fields=[
                ('road_coverage_id', models.AutoField(primary_key=True, serialize=False)),
                ('distance', models.FloatField()),
                ('year', models.IntegerField()),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.Counties')),
            ],
        ),
        migrations.CreateModel(
            name='Road_Coverage_Type_Distance_Ids',
            fields=[
                ('road_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('road_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='road_coverage_by_type_and_distance',
            name='road_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transport_and_communication.Road_Coverage_Type_Distance_Ids'),
        ),
        migrations.AddField(
            model_name='coverage_of_telephone_services',
            name='telephone_service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transport_and_communication.Coverage_Of_Telephone_Services_Ids'),
        ),
        migrations.AddField(
            model_name='coverage_of_postal_services',
            name='postal_service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transport_and_communication.Coverage_Of_Postal_Services_Ids'),
        ),
    ]
