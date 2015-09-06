from django.test import TestCase
from django.utils import timezone
from games.models import Game, Platform

class GameModelTest(TestCase):

    def setUp(self):
        self.platform = Platform(name='PC')
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
        Verify that the game descriptions are pulled in correctly only when
        the description is set to `tbd`.
        """
        game = Game(title="Hearthstone: Heroes of Warcraft",
        released=timezone.now(),
        platform=self.platform,
        description='This is not a real description')
        game.save()
        # Verify that the description was not saved
        self.assertEqual(game.description, 'This is not a real description')
        game.description = 'tbd'
        game.save()
        self.assertNotEqual(game.description, 'This is not a real description')
        self.assertNotEqual(game.description, 'tbd')
        self.assertNotEqual(game.description, '')

