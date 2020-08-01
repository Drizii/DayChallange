from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import ListView
from .models import Song, Day
from django.db.models import Q


def search_song_view(request):
    query = request.GET.get("q", None)
    qs = Song.objects.all().order_by('day')
    if query is not None:
        qs = qs.filter(
            Q(title__icontains=query) | Q(artist__icontains=query)
        )
    paginator = Paginator(qs.order_by('day'), 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    template_name = 'main.html'
    return render(request, template_name, context)
