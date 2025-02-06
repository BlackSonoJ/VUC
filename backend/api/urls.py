from django.urls import include, path
from rest_framework import routers
from .views import ImageViewSet, ImageMainPageViewSet, EventsViewSet


app_name = "api"

router = routers.DefaultRouter()
router.register(r"images", ImageViewSet)
router.register(r"imagesMainPage", ImageMainPageViewSet)
router.register(r"events", EventsViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
