from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HeartRateViewSet

router = DefaultRouter()
router.register(r"heart_rates", HeartRateViewSet)

urlpatterns = router.urls
