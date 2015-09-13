from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from users import views

urlpatterns = [
    url(r'^profile$', views.CurrentUserProfile.as_view(), name='current-profile'),
    url(r'^users$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<username>\w+)$', views.UserDetail.as_view(), name='user-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
