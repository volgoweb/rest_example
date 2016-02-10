# -*- coding: utf-8 -*-
# TODO Add caching list ids items of category, when will add filtering items by category.
from django.core.cache import cache


class CacheCollection(object):
    def __init__(self, object_type, serializer_class):
        self.object_type = object_type
        self.serializer_class = serializer_class

    def get_item_key(self, item_id):
        return '{}_{}'.format(self.object_type, item_id)

    def get(self, item_id):
        key = self.get_item_key(item_id)
        item = cache.get(key)
        return item

    def set(self, item_id, item):
        key = self.get_item_key(item_id)
        serializer = self.serializer_class(item)
        cache.set(key, serializer.data)

    def delete(self, item_id):
        key = self.get_item_key(item_id)
        cache.delete(key)
