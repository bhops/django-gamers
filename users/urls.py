from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
#    url(r'^users/$', views.GameList.as_view(), name='game-list'),
#   url(r'^users/(?P<pk>[0-9]+)/$', views.GameDetail.as_view(), name='game-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
