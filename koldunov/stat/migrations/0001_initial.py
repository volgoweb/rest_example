# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-08 17:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Population',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100, verbose_name='Country')),
                ('city', models.CharField(max_length=100, verbose_name='City')),
                ('population', models.IntegerField(verbose_name='Population')),
            ],
            options={
                'verbose_name': 'Population',
                'ordering': ['country'],
                'verbose_name_plural': 'Population',
            },
        ),
    ]
