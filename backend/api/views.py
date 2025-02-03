from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import ImageStorage
from .serializers import ImageStorageSerializer
from .permissions import IsOwnerOrReadOnly


class ImageStorageViewSet(viewsets.ModelViewSet):
    """Представление для профилей пользователей"""

    queryset = ImageStorage.objects.all()
    serializer_class = ImageStorageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
