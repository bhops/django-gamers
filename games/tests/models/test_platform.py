from django.test import TestCase
from games.models import Platform

class PlatformModelTest(TestCase):

    def test_string_representation(self):
        """
        Verify that Platforms appear with the appropriate string.
        """
        platform = Platform(name="PC")
        self.assertEqual(str(platform), platform.name)

    def test_verbose_name_plural(self):
        """
        Verify that the plural of `Platform` is `Platforms`.
        """
        self.assertEqual(str(Platform._meta.verbose_name_plural), "platforms")
