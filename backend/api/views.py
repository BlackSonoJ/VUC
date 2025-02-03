from rest_framework import viewsets, permissions

from .models import Images
from .serializers import ImagesSerializer


class ImageStorageViewSet(viewsets.ModelViewSet):
    """Представление для профилей пользователей"""

    queryset = Images.objects.all()
    serializer_class = ImagesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
