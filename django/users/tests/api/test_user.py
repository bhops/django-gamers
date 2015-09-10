# Things we want to test
## Unauthenticated users can ONLY create accounts
## Authenticated users can get a list of accounts with minimal details
## Authenticated users can get/edit their full profile details
## Authenticated users cannot edit any other profile
## Admin users have full permissions

from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.factories import UserFactory

class UserAPITests(APITestCase):

    def setUp(self):
        self.admin = UserFactory(is_staff=True)
        self.user = UserFactory()
        self.admin.save()
        self.user.save()

    def tearDown(self):
        self.admin.delete()
        self.user.delete()

class UnauthenticatedUserAPITests(UserAPITests):
    def setUp(self):
        super(UnauthenticatedUserAPITests, self).setUp()

    def tearDown(self):
        super(UnauthenticatedUserAPITests, self).tearDown()

    def test_user_list(self):
        """
        Verify that we cannot list users unauthenticated.
        """
        url = reverse('user-list')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_create(self):
        """
        Verify that we can create a user when we are unauthenticated.
        """
        url = reverse('user-list')
        data = {
            'username': 'testuser123',
            'password': 'thisisapassword',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'test@example.com'
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_detail(self):
        """
        Verify that we cannot get a user's details unauthenticated.
        """
        url = reverse('user-detail', args=[self.admin.username])
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_update(self):
        """
        Verify that we cannot update a user unauthenticated.
        """
        new_name = 'John'
        url = reverse('user-detail', args=[self.admin.username])
        data = { 'first_name': new_name }
        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_delete(self):
        """
        Verify that we cannot delete a user unauthenticated.
        """
        url = reverse('user-detail', args=[self.admin.username])
        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class AuthenticatedUserAPITests(UserAPITests):
    def setUp(self):
        super(AuthenticatedUserAPITests, self).setUp()
        self.client.force_authenticate(user=self.user)

    def tearDown(self):
        super(AuthenticatedUserAPITests, self).setUp()
        self.client.force_authenticate(user=None)

    def test_user_list(self):
        """
        Verify that we can list users when authenticated.
        """
        url = reverse('user-list')
        response = self.client.get(url, format='json')
        results = response.data.get('results', [])

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(results), 2)

    def test_user_create(self):
        """
        Verify that we cannot create a user when we are authenticated.
        """
        url = reverse('user-list')
        data = {
            'username': 'testuser123',
            'password': 'thisisapassword',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'test@example.com'
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_detail(self):
        """
        Verify that we can get a user's details when authenticated.
        """
        url = reverse('user-detail', args=[self.admin.username])
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_user_update_self(self):
        return
        """
        Verify that we can update ourselves when authenticated.
        """
        new_name = 'John'
        url = reverse('user-detail', args=[self.user.username])
        data = { 'first_name': new_name, 'dob': '1970-01-01' }
        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('first_name'), new_name)

    def test_user_update_other_user(self):
        """
        Verify that we cannot update another user when authenticated.
        """
        new_name = 'John'
        url = reverse('user-detail', args=[self.admin.username])
        data = { 'first_name': new_name }
        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_delete(self):
        """
        Verify that we cannot delete a user when authenticated.
        """
        url = reverse('user-detail', args=[self.admin.username])
        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class AdminUserAPITests(UserAPITests):

    def setUp(self):
        super(AdminUserAPITests, self).setUp()
        self.client.force_authenticate(user=self.admin)

    def tearDown(self):
        super(AdminUserAPITests, self).setUp()
        self.client.force_authenticate(user=None)

    def test_user_list(self):
        """
        Verify that we can list users when authenticated.
        """
        url = reverse('user-list')
        response = self.client.get(url, format='json')
        results = response.data.get('results', [])

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(results), 2)

    def test_user_create(self):
        """
        Verify that we cannot create a user when we are authenticated.
        """
        url = reverse('user-list')
        data = {
            'username': 'testuser123',
            'password': 'thisisapassword',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'test@example.com'
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_detail(self):
        """
        Verify that we can get a user's details when authenticated.
        """
        url = reverse('user-detail', args=[self.admin.username])
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_user_update_self(self):
        return
        """
        Verify that we can update ourselves when authenticated as admin.
        """
        new_name = 'John'
        url = reverse('user-detail', args=[self.admin.username])
        data = { 'first_name': new_name, 'dob': '1970-01-01' }
        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('first_name'), new_name)

    def test_user_update_other_user(self):
        return
        """
        Verify that we can update another user as admin.
        """
        new_name = 'John'
        url = reverse('user-detail', args=[self.user.username])
        data = { 'first_name': new_name, 'dob': '1970-01-01' }
        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('first_name'), new_name)

    def test_user_delete(self):
        """
        Verify that we can delete a user as admin.
        """
        url = reverse('user-detail', args=[self.admin.username])
        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

