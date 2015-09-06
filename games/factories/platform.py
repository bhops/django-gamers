import factory
from ..models import Platform

class PlatformFactory(factory.Factory):
    class Meta:
        model = Platform

    name = factory.Sequence(lambda n: 'platform%s' % n)
