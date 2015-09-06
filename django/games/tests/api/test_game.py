from django.core.urlresolvers import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase
from games.models import Game, Platform
from games.factories import GameFactory, PlatformFactory
from users.factories import UserFactory

class GameAPITests(APITestCase):
    def setUp(self):
        self.p1 = PlatformFactory()
        self.p2 = PlatformFactory()
        self.p1.save()
        self.p2.save()
        self.g1 = GameFactory(platform=self.p1)
        self.g2 = GameFactory(platform=self.p2)
        self.g1.save()
        self.g2.save()

    def tearDown(self):
        self.g1.delete()
        self.g2.delete()
        self.p1.delete()
        self.p2.delete()

class AuthenticatedGameAPITests(GameAPITests):
    def setUp(self):
        super(AuthenticatedGameAPITests, self).setUp()
        self.user = UserFactory()
        self.client.force_authenticate(user=self.user)

    def tearDown(self):
        super(AuthenticatedGameAPITests, self).tearDown()
        self.client.force_authenticate(user=None)

    def test_game_list(self):
        """
        Verify that we can query the list of games.
        """
        url = reverse('game-list')
        response = self.client.get(url, format='json')
        results = response.data.get('results', [])

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0].get('title'), self.g1.title)
        self.assertEqual(results[1].get('title'), self.g2.title)

    def test_game_create(self):
        """
        Verify that we cannot create a new game as regular user.
        """
        url = reverse('game-list')
        data = {
                'title': 'League of Legends',
                'platform': self.p1.slug,
                'description': 'description',
                'released': timezone.now()
            }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_game_detail(self):
        """
        Verify that we can query a single game.
        """
        url = reverse('game-detail', args=[self.g1.slug])
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('title'), self.g1.title)
        self.assertEqual(response.data.get('description'), self.g1.description)

    def test_game_update(self):
        """
        Verify that we cannot update a game as a regular user.
        """
        new_title = 'Not League of Legends'
        url = reverse('game-detail', args=[self.g1.slug])
        data = {
            'title': new_title,
            'platform': self.g1.platform.slug,
            'description': self.g1.description,
            'released': self.g1.released
        }
        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_game_delete(self):
        """
        Verify that we cannot delete a game as a regular user.
        """
        url = reverse('game-detail', args=[self.g1.slug])
        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class AdminGameAPITests(GameAPITests):
    def setUp(self):
        super(AdminGameAPITests, self).setUp()
        self.user = UserFactory(is_staff=True)
        self.client.force_authenticate(user=self.user)

    def tearDown(self):
        super(AdminGameAPITests, self).tearDown()
        self.client.force_authenticate(user=None)

    def test_game_list(self):
        """
        Verify that we can query the list of games.
        """
        url = reverse('game-list')
        response = self.client.get(url, format='json')
        results = response.data.get('results', [])

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0].get('title'), self.g1.title)
        self.assertEqual(results[1].get('title'), self.g2.title)

    def test_game_create(self):
        """
        Verify that we can create a new game as an admin.
        """
        url = reverse('game-list')
        data = {
                'title': 'League of Legends',
                'platform': self.p1.slug,
                'description': 'description',
                'released': timezone.now()
            }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_game_detail(self):
        """
        Verify that we can query a single game.
        """
        url = reverse('game-detail', args=[self.g1.slug])
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('title'), self.g1.title)
        self.assertEqual(response.data.get('description'), self.g1.description)

    def test_game_update(self):
        """
        Verify that we can update a game as an admin.
        """
        new_title = 'Not League of Legends'
        url = reverse('game-detail', args=[self.g1.slug])
        data = {
            'title': new_title,
            'platform': self.g1.platform.slug,
            'description': self.g1.description,
            'released': self.g1.released
        }
        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_game_delete(self):
        """
        Verify that we can delete a game as an admin.
        """
        url = reverse('game-detail', args=[self.g1.slug])
        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
