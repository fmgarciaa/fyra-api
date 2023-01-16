# Django Rest Framework


# Django
from django.urls import reverse

# Models
from fyra.customers.models.customers import Customer


class CRUDtoTestCase():
    """
    Class that allows us to inherit the functions of a CRUD: Create, Update and Delete.
    """

    def obj_create(self, url_set):
        url = reverse('{}:{}-list'.format(url_set, url_set))
        self.client.force_authenticate(self.user)
        response = self.client.post(url, self.data_create, format='json')
        self.assertEqual(response.status_code, 201)
        customer_name = response.data['name']
        obj = Customer.objects.get(name=customer_name)
        self.assertIsNotNone(obj)
        self.assertEqual(self.user.company_name, obj.company)
        return response.data['uuid']

    def obj_update(self, url_set):
        url = reverse('{}:{}-list'.format(url_set, url_set)) + self.uuid + "/"
        self.client.force_authenticate(self.user)
        response = self.client.patch(url, self.data_update, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['uuid'], self.uuid)

    def obj_delete(self, url_set):
        url = reverse('{}:{}-list'.format(url_set, url_set)) + self.uuid + "/"
        self.client.force_authenticate(self.user)
        response = self.client.delete(url)

        # Ensure that only owners company can delete objects
        self.assertFalse(self.user.is_owner)
        self.assertEqual(response.status_code, 403)

        # Change is_owner=True so that obj can be delete
        self.user.is_owner = True
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 200)

        customer = Customer.objects.get(uuid=self.uuid)
        self.assertTrue(customer.is_removed)
