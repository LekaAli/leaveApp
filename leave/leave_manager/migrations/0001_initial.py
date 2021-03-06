# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-05-25 09:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import leave_manager.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_number', models.CharField(max_length=12, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=10, null=True)),
                ('first_name', models.CharField(blank=True, max_length=25, null=True)),
                ('last_name', models.CharField(blank=True, max_length=35, null=True)),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employees',
            },
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('days_of_leave', models.SmallIntegerField(blank=True, null=True, validators=[leave_manager.models.daysOfLeave])),
                ('status', models.SmallIntegerField(choices=[(0, 'New'), (1, 'Approved'), (2, 'Declined')])),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='leave', to='leave_manager.Employee')),
            ],
            options={
                'verbose_name': 'Leave',
                'verbose_name_plural': 'Leaves',
            },
        ),
    ]
