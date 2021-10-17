import json
from datetime import date

from django.test import TestCase
from django.urls import reverse
from django.core import management
from django.contrib.auth import get_user_model

from rest_framework import status

User = get_user_model()


class OrderTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super(OrderTest, cls).setUpClass()
        management.call_command('load_test_data')
        cls.user = User.objects.last()
        cls.users_count = User.objects.count()
        cls.user_register_date = cls.user.registration_date
        cls.filtered_user = User.objects.filter(registration_date=cls.user_register_date)

    def test_get_list_users(self):
        self.url = reverse('order:api_v1_list_users')
        self.response = self.client.get(self.url)
        response_data = json.loads(self.response.content)
        self.expected_status = status.HTTP_200_OK
        self.response_status_code = self.response.status_code
        self.assertEqual(self.response_status_code, self.expected_status)
        self.assertEqual(len(response_data), self.users_count)
        for user in response_data:
            self.assertTrue(User.objects.get(first_name=user['first_name']))

    def test_get_users_by_date(self):
        self.url = reverse('order:api_v1_list_register_users', args=[self.user_register_date])
        self.response = self.client.get(self.url)
        response_data = json.loads(self.response.content)
        self.expected_status = status.HTTP_200_OK
        self.response_status_code = self.response.status_code
        self.assertEqual(self.response_status_code, self.expected_status)
        self.assertTrue(len(response_data))
        self.assertEqual(len(response_data), self.filtered_user.count())
        for user in response_data:
            self.assertTrue(self.filtered_user.get(first_name=user['first_name']))

    def test_get_request_with_unexisted_date(self):
        self.url = reverse('order:api_v1_list_register_users', args=[date(1111, 11, 11)])
        self.response = self.client.get(self.url)
        response_data = json.loads(self.response.content)
        self.expected_status = status.HTTP_200_OK
        self.response_status_code = self.response.status_code
        self.assertEqual(self.response_status_code, self.expected_status)
        self.assertFalse(len(response_data))