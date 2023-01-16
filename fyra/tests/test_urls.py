"""Urls test"""

# Django Rest Framework
from rest_framework.test import APITestCase

# Django
from django.urls import reverse


class URLTestCase(APITestCase):
    """
    Ensure that certain URL's needs Authentication
    """

    def fyra_urls(self, url_test):
        url = reverse('{}:{}-list'.format(url_test, url_test))
        response_list = self.client.get(url, format='json')
        response_post = self.client.post(url, format='json')
        self.assertEqual(response_list.status_code, 401)
        self.assertEqual(response_post.status_code, 401)
        code_list = response_list.data['detail'].code
        code_post = response_post.data['detail'].code
        self.assertEqual(code_list, 'not_authenticated')
        self.assertEqual(code_post, 'not_authenticated')

    def test_units_urls(self):
        self.fyra_urls('products')

    def test_categories_urls(self):
        self.fyra_urls('categories')

    def test_products_urls(self):
        self.fyra_urls('products')

    def test_customers_urls(self):
        self.fyra_urls('customers')

    def test_orders_urls(self):
        self.fyra_urls('orders')
