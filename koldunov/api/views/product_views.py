# -*- coding: utf-8 -*-
from rest_framework import viewsets

from koldunov.product.models import Category, Item
from koldunov.api.serializers.product_serializers import CategorySerializer, ItemSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

