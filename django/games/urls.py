from rest_framework import routers
from games import views

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'platforms', views.PlatformViewSet)
router.register(r'games', views.GameViewSet)

urlpatterns = router.urls
