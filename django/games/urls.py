#from django.conf.urls import url
from rest_framework import routers
#from rest_framework.urlpatterns import format_suffix_patterns
from games import views

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'platforms', views.PlatformViewSet)
router.register(r'games', views.GameViewSet)

urlpatterns = router.urls


#urlpatterns = [
#    url(r'^games$', views.GameList.as_view(), name='game-list'),
#    url(r'^games/(?P<slug>[-\w]+)$', views.GameDetail.as_view(), name='game-detail'),
#   url(r'^platforms$', views.PlatformList.as_view(), name='platform-list'),
#    url(r'^platforms/(?P<slug>[-\w]+)$', views.PlatformDetail.as_view(), name='platform-detail'),
#]

#urlpatterns = format_suffix_patterns(urlpatterns)
