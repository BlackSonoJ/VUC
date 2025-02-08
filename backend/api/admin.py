from django.contrib import admin

from .models import Images, ImagesMainPage, Events


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "image", "published"]


@admin.register(ImagesMainPage)
class ImagesMainPageAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "image", "published"]


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "name", "description", "published"]
