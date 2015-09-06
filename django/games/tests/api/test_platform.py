from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from games.models import Platform
from users.factories.user import UserFactory

class PlatformAPITests(APITestCase):

    def setUp(self):
        self.p1 = Platform(name='PC')
        self.p2 = Platform(name='PS4')
        self.p1.save()
        self.p2.save()

    def tearDown(self):
        self.p2.delete()
        self.p1.delete()

class AuthenticatedPlatformAPITests(PlatformAPITests):
    def setUp(self):
        super(AuthenticatedPlatformAPITests, self).setUp()
        self.user = UserFactory()
        self.client.force_authenticate(user=self.user)

    def tearDown(self):
        super(AuthenticatedPlatformAPITests, self).tearDown()
        self.client.force_authenticate(user=None)

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
        Verify that we cannot create a new platform as a normal user.
        """
        url = reverse('platform-list')
        data = {'name': 'Xbox One'}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

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
        Verify that we cannot update a platform as a normal user.
        """
        new_name = 'Not a PC'
        url = reverse('platform-detail', args=[self.p1.slug])
        data = { 'name': new_name }
        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_platform_delete(self):
        """
        Verify that we cannot delete a platform as a normal user.
        """
        url = reverse('platform-detail', args=[self.p1.slug])
        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
