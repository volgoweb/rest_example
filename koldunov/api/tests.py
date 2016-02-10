# -*- coding: utf-8 -*-
# TODO Add all necessary tests.
from collections import defaultdict
from django.test.testcases import TestCase
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

from ..product.models import Category, Item


class AuthTest(TestCase):
    def setUp(self):
        self.test_objects = defaultdict(list)

    def create_test_account(self):
        test_user = User.objects.create(
            username='test',
            email='test@test.test'
        )
        test_user.set_password('qwertyuio')
        self.test_objects['users'].append(test_user)

    def login(self):
        self.create_test_account()
        self.client = APIClient()
        result = self.client.login(username='test', password='qwertyuio')
        token = Token.objects.get(user__username='test')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        return result

    def test_post_category(self):
        self.login()
        url = '/app/api/category/'
        data = {
            'name': 'name1',
            'description': 'description1',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        cat = Category.objects.get(name='name1')
        self.assertEqual(cat.__str__(), 'name1')

    def create_test_category(self):
        self.test_objects['categories'].append(Category.objects.create(
            name='name_1',
            description='description_1'
        ))

    def test_get_category(self):
        self.login()
        self.create_test_category()
        orig_cat = self.test_objects.get('categories', [])[0]
        url = '/app/api/category/{}/'.format(orig_cat.pk)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'id': 1, 'name': orig_cat.name, 'description': orig_cat.description})
