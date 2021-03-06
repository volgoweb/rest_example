# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-14 19:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20160211_0959'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Stock',
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='item',
            name='categories',
            field=models.ManyToManyField(db_index=True, related_name='items_of_category', to='product.Category', verbose_name='Categories'),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(db_index=True, max_length=200, verbose_name='Name'),
        ),
    ]
