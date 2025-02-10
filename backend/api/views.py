from rest_framework import viewsets, permissions

from .models import Images, ImagesMainPage, Events, Videos
from .serializers import (
    ImagesSerializer,
    ImagesMainPageSerializer,
    EventsSerializer,
    VideosSerializer,
)

# Create your views here.


class ImagesViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ImagesMainPageViewSet(viewsets.ModelViewSet):
    queryset = ImagesMainPage.objects.all()
    serializer_class = ImagesMainPageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class EventsViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class VideosViewSet(viewsets.ModelViewSet):

    queryset = Videos.objects.all()
    serializer_class = VideosSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
