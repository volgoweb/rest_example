# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-08 18:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('stock', models.SmallIntegerField(blank=True, default=0, verbose_name='Stock')),
                ('cost', models.FloatField(verbose_name='Stock')),
                ('categories', models.ManyToManyField(to='product.Category', verbose_name='Categories')),
            ],
        ),
    ]
