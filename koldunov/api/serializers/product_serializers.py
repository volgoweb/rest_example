# -*- coding: utf-8 -*-
from rest_framework import serializers

from ...product import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)

    class Meta:
        model = models.Item
        fields = '__all__'
