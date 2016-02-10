# -*- coding: utf-8 -*-
from rest_framework import viewsets

from koldunov.population.models import Population
from koldunov.api.serializers.stat_serializers import StatSerializer


class StatViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Population.objects.all()
    serializer_class = StatSerializer
