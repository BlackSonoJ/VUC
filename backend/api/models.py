from django.db import models
from django.utils import timezone


class Images(models.Model):
    image_id = models.TextField()
    published = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.image_id}"

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"
