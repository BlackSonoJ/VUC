from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Images(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to="images/gallery", default=None)
    published = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.published}"

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"


class Events(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.TextField(max_length=250)
    description = models.TextField(blank=True)
    published = models.DateField(default=timezone.now)

    class Meta:
        ordering = ["published"]

        verbose_name = "Событие"
        verbose_name_plural = "События"

    def __str__(self):
        return f"{self.name}"


class ImagesMainPage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to="images/main", default=None)
    published = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.published}"

    class Meta:
        ordering = ["-published"]
        verbose_name = "Изображение на главной странице"
        verbose_name_plural = "Изображения на главной странице"


class Videos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    video = models.FileField(upload_to="videos/")
    published = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.published}"

    class Meta:
        ordering = ["-published"]
        verbose_name = "Видеоматериал"
        verbose_name_plural = "Видеоматериалы"
