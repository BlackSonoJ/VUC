from rest_framework import viewsets, permissions

from .models import Images, ImagesMainPage, Events
from .serializers import ImagesSerializer, ImagesMainPageSerializer, EventsSerializer


class ImageViewSet(viewsets.ModelViewSet):

    queryset = Images.objects.all()
    serializer_class = ImagesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ImageMainPageViewSet(viewsets.ModelViewSet):
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
