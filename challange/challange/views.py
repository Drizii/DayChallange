from .models import Person, Song
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic import CreateView
from django.db.models import Q


class SongListView(ListView):
    model = Song
    template_name = 'main.html'
    context_object_name = 'song_list'

    def get_song_queryset(query=None):
        queryset = []
        queries = query.split(" ")
        for q in queries:
            songs = Song.objects.filter(
                Q(title__incontains=q) |
                Q(artist__incontains=q) |
                Q(person__incontains=q)
            ).distinct()

        for song in songs:
            queryset.append(song)

        return list(set(queryset))