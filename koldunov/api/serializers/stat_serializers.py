# -*- coding: utf-8 -*-
from rest_framework import serializers

from koldunov.population.models import Population


class StatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Population
        fields = ('id', 'country', 'city', 'population')
        read_only_fields = fields

