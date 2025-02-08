from django.urls import path
from .views import (
    ImagesList,
    ImageDetail,
    ImagesMainPageList,
    ImageMainPageDetail,
    EventsList,
    EventDetail,
    VideosList,
    VideoDetail,
)


app_name = "api"


urlpatterns = [
    path("imagesMain/", ImagesMainPageList.as_view()),
    path("imagesMain/<int:pk>/", ImageMainPageDetail.as_view()),
    path("images/", ImagesList.as_view()),
    path("images/<int:pk>/", ImageDetail.as_view()),
    path("events/", EventsList.as_view()),
    path("events/<int:pk>/", EventDetail.as_view()),
    path("videos/", VideosList.as_view()),
    path("videos/<int:pk>/", VideoDetail.as_view()),
]
