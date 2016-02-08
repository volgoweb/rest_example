# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    description = models.TextField(verbose_name=_('Description'), null=True, blank=True)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        ordering = ['name']

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=200, verbose_name=_('Name'))
    categories = models.ManyToManyField('product.Category', verbose_name=_('Categories'))
    stock = models.SmallIntegerField(verbose_name=_('Stock'), blank=True, default=0)
    cost = models.FloatField(verbose_name=_('Cost'))

    class Meta:
        verbose_name = _('Item')
        verbose_name_plural = _('Items')
        ordering = ['name']

    def __str__(self):
        return self.name
