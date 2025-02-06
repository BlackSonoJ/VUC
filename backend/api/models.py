from django.db import models
from django.utils import timezone


class Images(models.Model):
    image = models.ImageField(upload_to="images/", default=None)
    published = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.published}"

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"
