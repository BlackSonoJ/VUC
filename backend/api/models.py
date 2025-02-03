from django.db import models
from django.utils import timezone


class ImageStorage(models.Model):
    image_id = models.TextField()
    published = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f"{self.image_id}"
