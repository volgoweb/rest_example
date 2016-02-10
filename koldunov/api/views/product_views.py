# -*- coding: utf-8 -*-
from rest_framework import viewsets

from ...product.models import Category, Item
from ..serializers.product_serializers import CategorySerializer, ItemSerializer
from ..mixins import CachedRetrieveMixin


class CategoryViewSet(CachedRetrieveMixin, viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ItemViewSet(CachedRetrieveMixin, viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

