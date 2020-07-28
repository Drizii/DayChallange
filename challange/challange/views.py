from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Song
from django.db.models import Q


def search_song_view(request):
    song_list = Song.objects.all()
    paginator = Paginator(song_list, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    query = request.GET.get("q", None)
    qs = Song.objects.all()
    if query is not None:
        qs = qs.filter(
            Q(title__icontains=query) | Q(artist__icontains=query)
        )
    context = {
        "song_list": qs,
        'page_obj': page_obj,
    }
    template_name = 'main.html'
    return render(request, template_name, context)

'''
def listing(request):
    song_list = Song.objects.all()
    paginator = Paginator(song_list, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'main.html', {'page_obj': page_obj})
'''