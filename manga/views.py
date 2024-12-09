from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Manga
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


def index(request):
    if request.user.is_authenticated:
        return redirect('manga_list')  # Redirect authenticated users to the manga list
    return render(request, 'public/index.html')  # Show public page for non-logged-in users


class MangaListView(LoginRequiredMixin, ListView):
    model = Manga
    template_name = 'manga/index.html'
    context_object_name = 'mangas'


class MangaCreateView(LoginRequiredMixin, CreateView):
    model = Manga
    template_name = 'manga/manga_form.html'
    fields = ['title', 'author', 'genre', 'status', 'chapters_read', 'total_chapters', 'start_date', 'end_date']
    success_url = reverse_lazy('manga_list')


class MangaUpdateView(LoginRequiredMixin, UpdateView):
    model = Manga
    template_name = 'manga/manga_form.html'
    fields = ['title', 'author', 'genre', 'status', 'chapters_read', 'total_chapters', 'start_date', 'end_date']
    success_url = reverse_lazy('manga_list')


class MangaDeleteView(LoginRequiredMixin, DeleteView):
    model = Manga
    template_name = 'manga/manga_confirm_delete.html'
    success_url = reverse_lazy('manga_list')


class MangaDetailView(LoginRequiredMixin, DetailView):
    model = Manga
    template_name = 'manga/manga_detail.html'
    context_object_name = 'manga'
