from rest_framework.routers import DefaultRouter
from restapi.views import SampleViewSet, TubeViewSet

router = DefaultRouter()
router.register(r'samples', SampleViewSet, basename='samples')
router.register(r'tubes', TubeViewSet, basename='tubes')

urlpatterns = router.urls