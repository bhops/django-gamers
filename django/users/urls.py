from rest_framework import routers
from users.views import Users

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'users', Users)

urlpatterns = router.urls
