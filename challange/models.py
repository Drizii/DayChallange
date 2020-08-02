from datetime import date
from django.db import models


class Event(models.Model):
    edition = models.CharField(max_length=128)

    def __str__(self):
        return self.edition


class Person(models.Model):
    name = models.CharField(verbose_name="Imie i nazwisko", max_length=128)

    def __str__(self):
        return self.name


class Song(models.Model):
    person = models.ForeignKey(Person, on_delete = models.CASCADE, verbose_name="Kto zaproponowal", default=None, blank=True)
    title = models.CharField(verbose_name="Tytuł", max_length=128)
    artist = models.CharField(verbose_name="Autor", max_length=128)
    link = models.URLField(verbose_name="Link do YT", db_index=True, unique=True, blank=True)

    def __str__(self):
        return self.artist + ' - ' + self.title


class Day(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name="Która edycja", default=None, blank=True)
    day = models.DateField(default=date.today)
    condition = models.CharField(verbose_name="Warunek", max_length=64, default="wybierz")
    song = models.ManyToManyField(Song, default=None, null=True)

    def __str__(self):
        return str(self.day)
