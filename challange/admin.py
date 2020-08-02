from django.contrib import admin
from .models import Song, Person, Day, Event


class SongTabularInLine(admin.TabularInline):
    model = Song
    extra = 3
    fields = ("person", "artist", "title", "link")


@admin.register(Day)
class DayAdmin(admin.ModelAdmin):
    inlines = [SongTabularInLine, ]

    class Meta:
        model = Day


admin.site.register(Person)
admin.site.register(Song)
admin.site.register(Event)
