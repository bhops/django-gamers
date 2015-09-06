import datetime
import factory
import factory.fuzzy
from ..models import Game
from .platform import PlatformFactory

class GameFactory(factory.Factory):
    class Meta:
        model = Game

    title = factory.Sequence(lambda n: 'game%s' % n)
    description = 'Description not available'
    platform = factory.SubFactory(PlatformFactory)
    released = factory.fuzzy.FuzzyDate(datetime.date(1990, 1, 1))
