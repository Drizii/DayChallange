from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Song
from django.db.models import Q


def search_song_view(request):
    song_list = Song.objects.all().order_by('-id')
    query = request.GET.get("q", None)
    qs = Song.objects.all().order_by('-id')
    if query is not None:
        qs = qs.filter(
            Q(title__icontains=query) | Q(artist__icontains=query)
        ).order_by('-id')
    paginator = Paginator(song_list, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
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