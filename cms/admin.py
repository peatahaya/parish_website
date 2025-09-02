from django.contrib import admin
from .models import News, Announcement, Intention


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "date")  # kolumny widoczne w liście
    search_fields = ("title", "content")  # pole wyszukiwania
    list_filter = ("date",)  # filtr po dacie
    ordering = ("-date",)  # sortowanie od najnowszych


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ("title", "date")
    search_fields = ("title", "content")
    list_filter = ("date",)
    ordering = ("-date",)


@admin.register(Intention)
class IntentionAdmin(admin.ModelAdmin):
    list_display = ("name", "date")
    search_fields = ("name", "prayer")
    list_filter = ("date",)
    ordering = ("-date",)
