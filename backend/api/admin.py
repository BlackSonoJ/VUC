from django.contrib import admin

from .models import Images


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ["id", "image_id", "published"]
