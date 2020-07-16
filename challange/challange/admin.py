from django.contrib import admin
from .models import Song, Person, Day, Event


admin.site.register(Person)
admin.site.register(Song)
admin.site.register(Day)
admin.site.register(Event)
