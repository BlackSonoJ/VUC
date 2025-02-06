from django.db import models


class Images(models.Model):
    image = models.ImageField(upload_to="images/", default=None)
    published = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.published}"

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"


class Events(models.Model):
    name = models.TextField(max_length=250)
    description = models.TextField(blank=True)
    published = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["published"]

        verbose_name = "Событие"
        verbose_name_plural = "События"

    def __str__(self):
        return f"{self.name}"


class ImagesMainPage(models.Model):
    image = models.ImageField(upload_to="images/main/", default=None)
    published = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.published}"

    class Meta:
        ordering = ["-published"]
        verbose_name = "Изображение на главной странице"
        verbose_name_plural = "Изображения на главной странице"
