from django.shortcuts import render
from .models import Song
from django.views.generic import ListView

from django.db.models import Q


class SongListView(ListView):
    model = Song
    template_name = 'main.html'
    context_object_name = 'song_list'


def search_song_view(request):
    query = request.GET.get("q", None)
    qs = Song.objects.all()
    if query is not None:
        qs = qs.filter(
            Q(title__icontains=query) | Q(artist__icontains=query)
        )
    context = {
        "song_list": qs,
    }
    template_name = 'main.html'
    return render(request, template_name, context)
