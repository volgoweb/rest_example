# -*- coding: utf-8 -*-
from rest_framework import viewsets

from ...stat.models import Population
from ..serializers import stat_serializers


class StatViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Population.objects.all()
    serializer_class = stat_serializers.StatSerializer
