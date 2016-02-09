# -*- coding: utf-8 -*-
from rest_framework import routers

from .views.product_views import CategoryViewSet, ItemViewSet
from .views.stat_views import StatViewSet

router = routers.SimpleRouter()
router.register(r'category', CategoryViewSet)
router.register(r'item', ItemViewSet)
router.register(r'stat', StatViewSet)

urlpatterns = router.urls
