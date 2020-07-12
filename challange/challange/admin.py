from django.contrib import admin
from .models import Song, Person


admin.site.register(Person)
admin.site.register(Song)
