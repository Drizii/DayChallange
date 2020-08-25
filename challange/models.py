from datetime import date
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Event(models.Model):
    edition = models.CharField(max_length=128)

    def __str__(self):
        return self.edition


class Person(models.Model):
    name = models.CharField(verbose_name="Imie i nazwisko", max_length=128)
    slug = models.SlugField(verbose_name="Slug - generowany automatycznie, zostaw puste.", default='', null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Person, self).save(*args, **kwargs)

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        return reverse("person-detail", args=[self.slug])

    def __str__(self):
        return self.name


class Day(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name="Która edycja", default=None, blank=True)
    date = models.DateField(default=date.today)
    condition = models.CharField(verbose_name="Warunek", max_length=128, default="wybierz")

    def __str__(self):
        return f"{self.date} - {self.condition}"


class Song(models.Model):
    person = models.ForeignKey(Person, on_delete = models.CASCADE, verbose_name="Kto zaproponowal", default=None, blank=True)
    title = models.CharField(verbose_name="Tytuł", max_length=128)
    artist = models.CharField(verbose_name="Autor", max_length=128)
    link = models.URLField(verbose_name="Link do YT", db_index=True, unique=True, blank=True)
    day = models.ForeignKey(Day, verbose_name="Dzień", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.artist} - {self.title}"
