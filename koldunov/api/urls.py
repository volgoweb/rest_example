# -*- coding: utf-8 -*-
from django.conf.urls import url

from .views.product_views import CategoryViewSet, ItemViewSet
from .views.stat_views import StatViewSet

urlpatterns = [
    url(r'^category/', CategoryViewSet),
    url(r'^item/', ItemViewSet),
    url(r'^stat/', StatViewSet),
]
