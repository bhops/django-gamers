from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone
from users.models import UserProfile

class UserProfileModelTest(TestCase):
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


    def TearDown(self):
        self.user.delete()
        self.user2.delete()

    def test_string_representation(self):
        """
        Verify that the string representation of UserProfile is correct.
        """
        self.assertEqual(str(self.user.profile), self.user.username)

    def test_verbose_name_plural(self):
        """
        Verify that the plural of User Profile is User Profiles.
        """
        self.assertEqual(str(UserProfile._meta.verbose_name_plural), "user profiles")


