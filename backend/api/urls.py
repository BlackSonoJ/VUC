from django.urls import include, path
from rest_framework import routers
from .views import ImageStorageViewSet


app_name = "api"

router = routers.DefaultRouter()
router.register(r"images", ImageStorageViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
