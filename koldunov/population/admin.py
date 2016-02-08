# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Population


class PopulationAdmin(admin.ModelAdmin):
    list_display = ('city', 'country', 'population')
    search_fields = ('country', 'city')
    list_filter = ('country',)


admin.site.register(Population, PopulationAdmin)