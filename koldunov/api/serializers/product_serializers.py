# -*- coding: utf-8 -*-
from rest_framework import serializers

from koldunov.product.models import Category, Item


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category


class ItemSerializer(serializers.ModelSerializer):
    # categories = serializers.HyperlinkedRelatedField(many=True)
    categories = serializers.SerializerMethodField()

    class Meta:
        model = Item

    def get_categories(self, obj):
        json_list = []
        for cat in obj.categories.all():
            cat_ser = CategorySerializer(cat)
            json_list.append(cat_ser.data)
        return json_list
