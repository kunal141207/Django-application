from rest_framework import routers
from .api import UserViewSet, ActivityPeriodViewSet

router = routers.DefaultRouter()
router.register('api/user', UserViewSet, 'user')
router.register('api/activity', ActivityPeriodViewSet, 'activity')

urlpatterns = router.urls
