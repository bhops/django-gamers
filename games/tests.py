import json

from django.core.urlresolvers import reverse
from django.test import TestCase
from django.utils import timezone
from .models import Game, Platform

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
        self.assertEqual(str(game), game.title + " ("+game.platform.name+")")

    def test_verbose_name_plural(self):
        """
        Verify that the plural of `Game` is `Games`.
        """
        self.assertEqual(str(Game._meta.verbose_name_plural), "games")


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


class GameTests(APITestCase):

    def setUp(self):
        self.p1 = Platform(name='PC', released=timezone.now())
        self.p2 = Platform(name='PS4', released=timezone.now())
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

    def test_create_game(self):
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



