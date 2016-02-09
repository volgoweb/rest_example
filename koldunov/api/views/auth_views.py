# -*- coding: utf-8 -*-
import logging
from django.middleware.csrf import _get_new_csrf_key
from django.contrib.auth import login
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


logger = logging.getLevelName(__name__)


class Login(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        login(request, user)
        response = Response({'token': token.key})
        csrf_token = _get_new_csrf_key()
        response.set_cookie('csrftoken', csrf_token)
        return response


