from datetime import date
from django.db import models


class Day(models.Model):
    day = models.DateField(date.today)
    condition = models.CharField(verbose_name="Warunek", max_length=64, default="wybierz")

    def __str__(self):
        return self.day


class Event(models.Model):
    edition = models.CharField(max_length=128)
    eventday = models.OneToOneField(Day, on_delete=models.CASCADE)

    def __str__(self):
        return self.edition


class Person(models.Model):
    name = models.CharField(verbose_name="Imie i nazwisko", max_length=128)

    def __str__(self):
        return self.name


class Song(models.Model):
    title = models.CharField(verbose_name="Tytuł", max_length=128)
    artist = models.CharField(verbose_name="Autor", max_length=128)
    link = models.URLField(verbose_name="Link do YT", db_index=True, unique=True, blank=True)
    person = models.ManyToManyField(Person, verbose_name="Kto zaproponowal")
    event = models.ManyToManyField(Event, verbose_name="Która edycja", default="wybierz")

    def __str__(self):
        return self.artist + ' - ' + self.title

