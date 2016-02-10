# -*- coding: utf-8 -*-
# TODO Move cache updating code to celery-task
from django.conf import settings
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete, m2m_changed

from ..product.models import Category, Item
from ..stat.models import Population
from .cache import CacheCollection
from .serializers.product_serializers import CategorySerializer, ItemSerializer
from .serializers.stat_serializers import StatSerializer


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


def update_cache_simple(instance, serializer_class):
    collection = CacheCollection(instance.__class__.__name__, serializer_class)
    collection.set(instance.pk, instance)


def delete_cache_simple(instance, serializer_class):
    collection = CacheCollection(instance.__class__.__name__, serializer_class)
    collection.delete(instance.pk)


@receiver(post_save, sender=Category)
def update_category_cache(instance, *args, **kwargs):
    update_cache_simple(instance, CategorySerializer)

    items_with_category = Item.objects.all().has_any_category([instance])
    item_collection = CacheCollection('item', ItemSerializer)
    for item in items_with_category:
        item_collection.set(item.pk, item)


@receiver(post_delete, sender=Category)
def delete_category_cache(instance, *args, **kwargs):
    delete_cache_simple(instance, CategorySerializer)

    items_with_category = Item.objects.all().has_any_category([instance])
    item_collection = CacheCollection(Item.__name__, ItemSerializer)
    for item in items_with_category:
        item_collection.set(item.pk, item)


@receiver(m2m_changed, sender=Item.categories.through)
def update_item_cahce(action, instance, *args, **kwargs):
    update_cache_simple(instance, ItemSerializer)


@receiver(post_save, sender=Item)
def update_item_cache(instance, *args, **kwargs):
    update_cache_simple(instance, ItemSerializer)


@receiver(post_delete, sender=Item)
def delete_item_cache(instance, *args, **kwargs):
    delete_cache_simple(instance, ItemSerializer)


@receiver(post_save, sender=Population)
def update_population_cache(instance, *args, **kwargs):
    update_cache_simple(instance, StatSerializer)


@receiver(post_delete, sender=Population)
def delete_item_cache(instance, *args, **kwargs):
    delete_cache_simple(instance, StatSerializer)

