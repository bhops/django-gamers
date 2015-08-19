from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from games import views

urlpatterns = [
    url(r'^games/$', views.GameList.as_view(), name='game-list'),
    url(r'^games/(?P<pk>[0-9]+)/$', views.GameDetail.as_view(), name='game-detail'),
    url(r'^platforms/$', views.PlatformList.as_view(), name='platform-list'),
    url(r'^platforms/(?P<pk>[0-9]+)/$', views.PlatformDetail.as_view(), name='platform-detail'),
    url(r'^games/owned/(?P<username>\w+)/$', views.OwnedGameList.as_view(), name='owned-game-list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
