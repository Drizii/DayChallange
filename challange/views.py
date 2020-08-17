from datetime import datetime, timedelta, date

from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Song, Day, Person
from django.db.models import Q


def search_song_view(request):
    query = request.GET.get("q", None)
    qs = Song.objects.all()
    if query is not None:
        qs = qs.filter(
            Q(title__icontains=query) | Q(artist__icontains=query)
        )
        paginator = Paginator(qs.order_by('artist'), 25)
    else:
        paginator = Paginator(qs.order_by('-day__date', 'artist'), 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    template_name = 'main.html'
    return render(request, template_name, context)


class DayListView(ListView):
    model = Day
    template_name = "day.html"
    context_object_name = "day"
    paginate_by = 5
    ordering = ['-date', 'id']


class PersonDetailView(DetailView):
    model = Person
    template_name = "person_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["days"] = self.get_days()
        return context

    def get_days(self):
        days_count = 100
        start_date = date(2020, 7, 27)
        days_list = self.__get_person_days()
        active_days = []
        for i in range(days_count):
            today = start_date + timedelta(days=i)
            active_day = {
                "date": today,
                "active": self.__is_active(today, days_list),
            }
            active_days.append(active_day)
        return active_days

    def __get_person_days(self):
        person_songs = self.object.song_set.all()
        days_list = []
        for song in person_songs:
            days_list.append(song.day.date)
        return days_list

    def __is_active(self, today, days_list):
        return today in days_list


