# -*- coding: utf-8 -*-
from rest_framework.response import Response
from .cache import CacheCollection


class CachedRetrieveMixin(object):
    def retrieve(self, request, *args, **kwargs):
        model_name = self.serializer_class.Meta.model.__name__
        collection = CacheCollection(model_name, self.serializer_class)
        cached_object = collection.get(kwargs.get('pk'))
        if cached_object:
            return Response(cached_object)

        return super(CachedRetrieveMixin, self).retrieve(request, *args, **kwargs)
