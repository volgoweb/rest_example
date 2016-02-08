# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Category, Item


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'description')


admin.site.register(Category, CategoryAdmin)


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'stock', 'cost')
    search_fields = ('name',)
    list_filter = ('categories',)


admin.site.register(Item, ItemAdmin)
