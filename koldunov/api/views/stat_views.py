# -*- coding: utf-8 -*-
from rest_framework import viewsets

from koldunov.population.models import Population
from koldunov.api.serializers.stat_serializers import StatSerializer
from koldunov.api.permissions import ReadOnly


class StatViewSet(viewsets.ModelViewSet):
    queryset = Population.objects.all()
    serializer_class = StatSerializer
    permission_classes = [ReadOnly]
