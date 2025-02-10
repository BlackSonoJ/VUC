from django.urls import include, path
from rest_framework import routers

from .views import ImagesViewSet, ImagesMainPageViewSet, EventsViewSet, VideosViewSet

app = "api"

router = routers.DefaultRouter()
router.register(r"images", ImagesViewSet)
router.register(
    r"imagesMain",
    ImagesMainPageViewSet,
)
router.register(r"events", EventsViewSet)
router.register(r"videos", VideosViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
