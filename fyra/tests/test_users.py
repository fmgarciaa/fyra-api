"""User test"""

# Django Rest Framework
from rest_framework.test import APITestCase

# Django
from django.urls import reverse

# Models
from fyra.users.models.users import User


class SignUpUserTestCase(APITestCase):
    """
    Ensure we can create a new user.
    """

    def setUp(self):
        self.data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'phone_number': "990099990",
            'password': 'test1245',
            'password_confirmation': 'test1245',
            'first_name': 'Test',
            'last_name': 'User',
            'company_name': 'TestCase Inc'
        }

    def test_create_user(self):
        url = reverse('users:users-signup')
        response = self.client.post(url, self.data, format='json')
        self.assertEqual(response.status_code, 201)
        username_new_user = response.data['username']
        user = User.objects.get(username=username_new_user)
        self.assertEqual(user.username, self.data['username'])
        self.assertEqual(user.email, self.data['email'])
        self.assertTrue(user.check_password(self.data['password']))


class LoginUserTestCast(APITestCase):
    """
    Ensure that a user can log in
    """

    def setUp(self):
        self.username = 'testuser'
        self.email = 'testuser@example.com'
        self.password = 'testpassword'
        self.user = User.objects.create_user(self.username, self.email, self.password, is_verified=True)

    def test_login_user(self):
        url = reverse('users:users-login')
        data = {
            'email': self.email, 'password': self.password
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertTrue('access_token' in response.data)
        token = response.data['access_token']
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        url = '/api/users/{}'.format(self.username)
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)
