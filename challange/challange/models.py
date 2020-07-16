from django.db import models


class Edition:
    SongNameByLetter = 1
    ArtistNameByLetter = 2
    Choice = {
        SongNameByLetter: "Piosenka na literę...",
        ArtistNameByLetter: "Artysta na literę...",
    }


class Person(models.Model):
    name = models.CharField(verbose_name="Imie i nazwisko", max_length=111)

    def __str__(self):
        return self.name


class Day(models.Model):
    day = models.DateField()


class Song(models.Model):
    title = models.CharField(verbose_name="Tytuł", max_length=111)
    artist = models.CharField(verbose_name="Autor", max_length=111)
    link = models.URLField(verbose_name="Link do YT", db_index=True, unique=True, blank=True)
    person = models.ManyToManyField(Person, verbose_name="Kto zaproponowal")
    edition = models.PositiveSmallIntegerField(choices=Edition.Choice.items(), verbose_name="Która edycja")

    def __str__(self):
        return self.artist + ' - ' + self.title

