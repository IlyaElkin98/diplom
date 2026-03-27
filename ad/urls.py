from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ad.apps import AdConfig
from ad.views import AdViewSet

app_name = AdConfig.name

router = DefaultRouter()
router.register(r'ad', AdViewSet)

urlpatterns = [
    path('', include(router.urls))
]
