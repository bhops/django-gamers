from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from matchups import views

urlpatterns = [
    url(r'^matchups/$', views.LookingForPostList.as_view(), name='matchup-list'),
    url(r'^matchups/(?P<pk>\w+)\/$', views.LookingForPostDetail.as_view(), name='matchup-detail'),
    url(r'^games/(?P<game>\w+)\/matchups$', views.LookingForPostListGame.as_view(), name='matchup-game-list'),
    url(r'^schedules/(?P<username>\w+)\/$', views.ScheduleDetail.as_view({'get': 'retrieve'}), name='schedule-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
