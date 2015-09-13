from django.test import TestCase
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
