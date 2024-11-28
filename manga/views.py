from django.shortcuts import render
from .models import Manga
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy


def index(request):
    mangas = Manga.objects.all()
    return render(request, 'manga/index.html', {'mangas': mangas})


class MangaListView(ListView):
    model = Manga
    template_name = 'manga/index.html'
    context_object_name = 'mangas'


class MangaCreateView(CreateView):
    model = Manga
    template_name = 'manga/manga_form.html'
    fields = ['title', 'author', 'genre', 'status', 'chapters_read', 'total_chapters', 'start_date', 'end_date']
    success_url = reverse_lazy('index')


class MangaUpdateView(UpdateView):
    model = Manga
    template_name = 'manga/manga_form.html'
    fields = ['title', 'author', 'genre', 'status', 'chapters_read', 'total_chapters', 'start_date', 'end_date']
    success_url = reverse_lazy('index')


class MangaDeleteView(DeleteView):
    model = Manga
    template_name = 'manga/manga_confirm_delete.html'
    success_url = reverse_lazy('index')


class MangaDetailView(DetailView):
    model = Manga
    template_name = 'manga/manga_detail.html'
    context_object_name = 'manga'
