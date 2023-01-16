"""Create Products, Customers and Orders case """

# Utils
from fyra.utils.crud_to_tests import CRUDtoTestCase
from rest_framework.test import APITestCase
from fyra.users.models.users import User


class CustomerObjTestCase(APITestCase):
    """
    """

    crud_test = CRUDtoTestCase

    def setUp(self):
        self.data_user = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpassword',
            'company_name': 'TestCase Inc',
            'first_name': 'Test',
            'last_name': 'User'
        }
        self.user = User.objects.create(**self.data_user, is_verified=True)

        self.data_create = {
            "name": "Joe Doe",
            "phone": "990990990",
            "email": "joedoe@io.com",
            "address": "123 Maple Street",
            "reference": "Any where",
            "district": "Anytown",
            "province": "Washington",
            "department": "EEUU"
        }

        self.data_update = {
            'name': 'Jose Durant'
        }

    def test_customer_create(self):
        self.crud_test.obj_create(self, 'customers')

    def test_customer_update(self):
        self.uuid = self.crud_test.obj_create(self, 'customers')
        self.crud_test.obj_update(self, 'customers')

    def test_customer_delete(self):
        self.uuid = self.crud_test.obj_create(self, 'customers')
        self.crud_test.obj_delete(self, 'customers')
