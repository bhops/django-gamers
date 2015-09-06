import datetime
import factory
import factory.fuzzy
from django.contrib.auth.models import User
from ..models import UserProfile

class UserFactory(factory.Factory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: 'testuser%s' % n)
    first_name = 'John'
    last_name = 'Doe'
    email = factory.LazyAttribute(lambda o: '%s@example.org' % o.username)
    is_staff = False

class UserProfileFactory(factory.Factory):
    class Meta:
        model = UserProfile

    user = factory.SubFactory(UserFactory)
    dob = factory.fuzzy.FuzzyDate(datetime.date(1960, 1, 1))
    sex = 'M'
