from django.shortcuts import render
from .models import Song
from django.views.generic import ListView

from django.db.models import Q


class SongListView(ListView):
    model = Song
    template_name = 'main.html'
    context_object_name = 'song_list'

    def search_song_view(self, request):
        query = request.GET.get("q", None)
        qs = Song.objects.all()
        if query is not None:
            qs = qs.filter(
                Q(title__icontains=query) | Q(artist__icontains=query)
            )
        context = {
            "object_list": qs,
        }
        return render(request, context)

'''
class SongSearchView(ListView):
    model = Song
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q', None)
        return Song.objects.filter(
            Q(title__icontains=query) | Q(artist__icontains=query)
        )
        if query is None:
            return object_list
'''