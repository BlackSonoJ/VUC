from rest_framework import permissions
from rest_framework import generics

from .models import Images, ImagesMainPage, Events, Videos
from .serializers import (
    ImagesSerializer,
    ImagesMainPageSerializer,
    EventsSerializer,
    VideosSerializer,
)


class ImagesList(generics.ListCreateAPIView):

    queryset = Images.objects.all()
    serializer_class = ImagesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ImagesMainPageList(generics.ListCreateAPIView):
    queryset = ImagesMainPage.objects.all()
    serializer_class = ImagesMainPageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ImageMainPageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ImagesMainPage.objects.all()
    serializer_class = ImagesMainPageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class EventsList(generics.ListCreateAPIView):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class VideosList(generics.ListCreateAPIView):

    queryset = Videos.objects.all()
    serializer_class = VideosSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class VideoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Videos.objects.all()
    serializer_class = VideosSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
