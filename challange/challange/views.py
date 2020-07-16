from .models import Song
from django.views.generic import ListView

from django.db.models import Q


class SongListView(ListView):
    model = Song
    template_name = 'main.html'
    context_object_name = 'song_list'


class SongSearchView(ListView):
    model = Song
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Song.objects.filter(
            Q(title__icontains=query) | Q(artist__icontains=query)
        )
        return object_list
