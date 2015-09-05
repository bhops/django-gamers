from django.core.urlresolvers import reverse
from games.models import Platform
from rest_framework import status
from rest_framework.test import APITestCase

class PlatformApiTests(APITestCase):

    def setUp(self):
        self.p1 = Platform(name='PC')
        self.p2 = Platform(name='PS4')
        self.p1.save()
        self.p2.save()
    def tearDown(self):
        self.p2.delete()
        self.p1.delete()

    def test_platform_list(self):
        """
        Verify that we can query the list of platforms.
        """
        url = reverse('platform-list')
        response = self.client.get(url, format='json')
        results = response.data.get('results', [])

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0].get('name'), self.p1.name)
        self.assertEqual(results[1].get('name'), self.p2.name)

    def test_platform_create(self):
        """
        Verify that we can create a new platform.
        """
        url = reverse('platform-list')
        data = {
            'name': 'Xbox One',
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual('Xbox One', response.data.get('name'))

    def test_platform_detail(self):
        """
        Verify that we can query a single platform.
        """
        url = reverse('platform-detail', args=[self.p1.slug])
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('name'), self.p1.name)

    def test_platform_update(self):
        """
        Verify that we can update a platform.
        """
        new_name = 'Not a PC'
        url = reverse('platform-detail', args=[self.p1.slug])
        data = { 'name': new_name }
        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('name'), new_name)

    def test_platform_delete(self):
        """
        Verify that we can delete a platform.
        """
        url = reverse('platform-detail', args=[self.p1.slug])
        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.data, None)

        # Check for the platform on the list.
        url = reverse('platform-list')
        response = self.client.get(url, format='json')
        results = response.data.get('results', [])

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].get('name'), self.p2.name)

