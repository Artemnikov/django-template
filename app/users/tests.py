from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import User
from .serializers import baseUserSerializer

class UserTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            'username': 'test@example.com',
            'email_adress': 'test@example.com',
            'password': 'mypassword',
            'first_name': 'John',
            'last_name': 'Doe',
            'phone': '1234567890'
        }
        self.user = User.objects.create_user(**self.user_data)
        self.url = reverse('user-list')

    def test_create_user(self):
        response = self.client.post(self.url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)

    def test_get_user_list(self):
        response = self.client.get(self.url)
        users = User.objects.all()
        serializer = baseUserSerializer(users, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_user_detail(self):
        response = self.client.get(reverse('user-detail', args=[self.user.id]))
        user = User.objects.get(id=self.user.id)
        serializer = baseUserSerializer(user)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_user(self):
        updated_data = {
            'first_name': 'Updated Name',
            'last_name': 'Updated Last Name'
        }
        response = self.client.put(reverse('user-detail', args=[self.user.id]), updated_data, format='json')
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, updated_data['first_name'])
        self.assertEqual(self.user.last_name, updated_data['last_name'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_user(self):
        response = self.client.delete(reverse('user-detail', args=[self.user.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
