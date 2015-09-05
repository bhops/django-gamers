from django.conf.urls import include, url

urlpatterns = [
    url(r'^', include('games.urls')),
    url(r'^', include('users.urls')),
]

