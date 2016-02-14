# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Name'), db_index=True)
    description = models.TextField(verbose_name=_('Description'), null=True, blank=True)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        ordering = ['name']

    def __str__(self):
        return self.name


class ItemQueryset(models.query.QuerySet):
    def has_any_category(self, categories):
        return self.filter(categories__in=categories)


class ItemManager(models.Manager):
    def get_queryset(self):
        return ItemQueryset(self.model).all()


class Item(models.Model):
    name = models.CharField(max_length=200, verbose_name=_('Name'), db_index=True)
    categories = models.ManyToManyField('product.Category', verbose_name=_('Categories'),
                                        related_name='items_of_category', db_index=True)
    stock = models.SmallIntegerField(verbose_name=_('Stock'), blank=True, default=0)
    cost = models.FloatField(verbose_name=_('Cost'))

    objects = ItemManager()

    class Meta:
        verbose_name = _('Item')
        verbose_name_plural = _('Items')
        ordering = ['name']

    def __str__(self):
        return self.name
