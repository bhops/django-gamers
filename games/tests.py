from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone
from .models import Game, OwnedGame, Platform
from rest_framework import status
from rest_framework.test import APITestCase

class GameModelTest(TestCase):

    def setUp(self):
        self.platform = Platform(name='PC', released=timezone.now())
        self.platform.save()

    def tearDown(self):
        self.platform.delete()

    def test_string_representation(self):
        """
        Verify that games appear with the appropriate string.
        """
        game = Game(title="My Game Title", platform=self.platform)
        self.assertEqual(str(game), "["+game.platform.name+"] " + game.title)

    def test_verbose_name_plural(self):
        """
        Verify that the plural of `Game` is `Games`.
        """
        self.assertEqual(str(Game._meta.verbose_name_plural), "games")

    def test_description_pull(self):
        """
        Verify that the game descriptions are pulled in correctly only when description is set to `tbd`.
        """
        game = Game(title="Hearthstone: Heroes of Warcraft",
                    released=timezone.now(),
                    platform=self.platform,
                    description='This is not a real description')
        game.save()
        self.assertEqual(game.description, 'This is not a real description') # Verify that the description is unchanged
        game.description = 'tbd'
        game.save()
        self.assertNotEqual(game.description, 'This is not a real description')
        self.assertNotEqual(game.description, 'tbd')
        self.assertNotEqual(game.description, '')


class PlatformModelTest(TestCase):

    def test_string_representation(self):
        """
        Verify that Platforms appear with the appropriate string.
        """
        platform = Platform(name="PC", released=timezone.now())
        self.assertEqual(str(platform), platform.name)

    def test_verbose_name_plural(self):
        """
        Verify that the plural of `Platform` is `Platforms`.
        """
        self.assertEqual(str(Platform._meta.verbose_name_plural), "platforms")


class GameAndPlatformTests(APITestCase):

    def setUp(self):
        self.p1 = Platform(name='PC', company='N/A', description='A random computer', released=timezone.now())
        self.p2 = Platform(name='PS4', company='Sony', description='Sony Playstation 4', released=timezone.now())
        self.p1.save()
        self.p2.save()
        self.g1 = Game(title='Hearthstone',
                       platform=self.p1,
                       description='Hearthstone by Blizzard',
                       released=timezone.now())
        self.g2 = Game(title='Battlefield 4',
                       platform=self.p2,
                       description='EA Games',
                       released=timezone.now())
        self.g1.save()
        self.g2.save()

    def tearDown(self):
        self.g2.delete()
        self.g1.delete()
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
            'company': 'Microsoft',
            'description': 'Xbox One by Microsoft',
            'released': timezone.now()
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('released', response.data)
        self.assertIn('description', response.data)
        self.assertEqual('Microsoft', response.data.get('company'))
        self.assertEqual('Xbox One', response.data.get('name'))

    def test_platform_detail(self):
        """
        Verify that we can query a single platform.
        """
        url = reverse('platform-detail', args=[self.p1.id])
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('name'), self.p1.name)
        self.assertEqual(response.data.get('description'), self.p1.description)

    def test_platform_update(self):
        """
        Verify that we can update a platform.
        """
        new_name = 'Not a PC'
        url = reverse('platform-detail', args=[self.p1.id])
        data = {
            'name': new_name,
            'company': self.p1.company,
            'description': self.p1.description
        }
        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('company'), self.p1.company)
        self.assertEqual(response.data.get('description'), self.p1.description)
        self.assertEqual(response.data.get('name'), new_name)

    def test_platform_delete(self):
        """
        Verify that we can delete a platform.
        """
        url = reverse('platform-detail', args=[self.p1.id])
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

    def test_game_list(self):
        """
        Verify that we can query the list of games.
        """
        url = reverse('game-list')
        response = self.client.get(url, format='json')
        results = response.data.get('results', [])

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0].get('title'), self.g2.title)
        self.assertEqual(results[1].get('title'), self.g1.title)

    def test_game_create(self):
        """
        Verify that we can create a new game.
        """
        url = reverse('game-list')
        data = {
                'title': 'League of Legends',
                'platform': self.p1.id,
                'description': 'description',
                'released': timezone.now()
            }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('platform', response.data)
        self.assertIn('released', response.data)
        self.assertIn('description', response.data)
        self.assertEqual('League of Legends', response.data.get('title'))

    def test_game_detail(self):
        """
        Verify that we can query a single game.
        """
        url = reverse('game-detail', args=[self.g1.id])
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('title'), self.g1.title)
        self.assertEqual(response.data.get('description'), self.g1.description)

    def test_game_update(self):
        """
        Verify that we can update a game.
        """
        new_title = 'Not League of Legends'
        url = reverse('game-detail', args=[self.g1.id])
        data = {
            'title': new_title,
            'platform': self.g1.platform.id,
            'description': self.g1.description,
            'released': self.g1.released
        }
        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('description'), self.g1.description)
        self.assertEqual(response.data.get('title'), new_title)

    def test_game_delete(self):
        """
        Verify that we can delete a platform.
        """
        url = reverse('game-detail', args=[self.g1.id])
        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.data, None)

        # Check for the game on the list.
        url = reverse('game-list')
        response = self.client.get(url, format='json')
        results = response.data.get('results', [])

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].get('title'), self.g2.title)

class OwnedGameModelTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testing123'
        )
        self.user2 = User.objects.create_user(
            username='anothertest',
            email='another@example.com',
            password='testing321'
        )
        self.user.save()
        self.user2.save()
        self.p1 = Platform(name='PC', company='N/A', description='A random computer', released=timezone.now())
        self.p2 = Platform(name='PS4', company='Sony', description='Sony Playstation 4', released=timezone.now())
        self.p1.save()
        self.p2.save()
        self.g1 = Game(title='Hearthstone: Heroes of Warcraft',
                    platform=self.p1,
                    description='Hearthstone by Blizzard',
                    released=timezone.now())
        self.g2 = Game(title='Battlefield 4',
                    platform=self.p2,
                    description='EA Games',
                    released=timezone.now())
        self.g1.save()
        self.g2.save()
        self.og1 = OwnedGame(user=self.user, game=self.g1)
        self.og2 = OwnedGame(user=self.user, game=self.g2)
        self.og3 = OwnedGame(user=self.user2, game=self.g1)
        self.og1.save()
        self.og2.save()
        self.og3.save()

    def tearDown(self):
        self.og1.save()
        self.og2.save()
        self.og3.save()
        self.g2.delete()
        self.g1.delete()
        self.p2.delete()
        self.p1.delete()
        self.user.delete()
        self.user2.delete()

    def test_string_representation(self):
        """
        Verify that the string representation of OwnedGame is correct.
        """
        og = OwnedGame(user=self.user, game=self.g1)
        self.assertEqual(str(og), '[testuser] Hearthstone: Heroes of Warcraft')

    def test_verbose_name_plural(self):
        """
        Verify that plural of `owned game` is `owned games`.
        """
        self.assertEqual(str(OwnedGame._meta.verbose_name_plural), "owned games")

    def test_ownedgame_list(self):
        """
        Verify that we can query the list of owned games for a user.
        """
        url = reverse('owned-game-list', args=[self.user.username])
        response = self.client.get(url, format='json')
        results = response.data.get('results', [])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0].get('game').get('title'), self.g1.title)
        self.assertEqual(results[1].get('game').get('title'), self.g2.title)

        url = reverse('owned-game-list', args=[self.user2.username])
        response = self.client.get(url, format='json')
        results = response.data.get('results', [])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].get('game').get('title'), self.g1.title)

