from django.db import models


class Person(models.Model):
    name = models.CharField(verbose_name="Imie i nazwisko", max_length=111)

    def __str__(self):
        return self.name


class Song(models.Model):
    title = models.CharField(verbose_name="Tytuł", max_length=111)
    artist = models.CharField(verbose_name="Autor", max_length=111)
    link = models.URLField(verbose_name="Link do YT", db_index=True, unique=True, blank=True)
    person = models.ManyToManyField(Person, verbose_name="Kto zaproponowal")

    def __str__(self):
        return self.artist + ' - ' + self.title

