# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Population(models.Model):
    country = models.CharField(max_length=100, verbose_name=_('Country'))
    city = models.CharField(max_length=100, verbose_name=_('City'))
    population = models.IntegerField(verbose_name=_('Population'))

    class Meta:
        verbose_name = _('Population')
        verbose_name_plural = _('Population')
        ordering = ['country']

    def __str__(self):
        return '{}, {}: {}'.format(self.country, self.city, self.population)
