from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import UpdateView, DeleteView, ListView, CreateView, DetailView
from django.urls import reverse_lazy
from .models import Manga, Comment, Rating
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CommentForm, MangaForm, SearchForm, RatingForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


class MangaListView(ListView):
    model = Manga
    template_name = 'manga/index.html'
    context_object_name = 'mangas'
    paginate_by = 10  # Add pagination if needed

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SearchForm(self.request.GET)
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        form = SearchForm(self.request.GET)

        if form.is_valid() and form.cleaned_data.get('query'):
            query = form.cleaned_data['query']
            queryset = queryset.filter(title__icontains=query)

        return queryset


class AddMangaView(CreateView):
    model = Manga
    form_class = MangaForm
    template_name = 'manga/manga_form.html'
    success_url = reverse_lazy('manga_list')  # Redirect to the manga list after successful creation

    def form_valid(self, form):
        # Any additional logic (e.g., logging, modifying form data) can go here before saving
        return super().form_valid(form)


class MangaUpdateView(UpdateView):
    model = Manga
    fields = ['title', 'author', 'genre', 'status', 'chapters_read', 'total_chapters', 'start_date', 'end_date', 'cover_image']
    template_name = 'manga/manga_form.html'
    success_url = reverse_lazy('manga_list')


class MangaDeleteView(LoginRequiredMixin, DeleteView):
    model = Manga
    template_name = 'manga/manga_confirm_delete.html'
    success_url = reverse_lazy('index')


def manga_detail(request, manga_id):
    manga = get_object_or_404(Manga, id=manga_id)
    context = {'manga': manga, 'form': CommentForm(), 'comments': manga.comments.all(), 'rating_form': RatingForm()}

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        rating_form = RatingForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.manga = manga
            comment.save()
            return redirect('manga_detail', manga_id=manga.id)

        # Handle invalid comment form (optional: show errors in template)

        if rating_form.is_valid():
            rating = rating_form.cleaned_data['rating']  # Access validated data
            # Check if the user has already rated this manga
            existing_rating = Rating.objects.filter(manga=manga, user=request.user).first()
            if existing_rating:
                existing_rating.rating = rating
                existing_rating.save()
            else:
                new_rating = Rating.objects.create(manga=manga, user=request.user, rating=rating)
            return redirect('manga_detail', manga_id=manga.id)

        # Handle invalid rating form (optional: show errors in template)

    return render(request, 'manga/manga_detail.html', context)


@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if request.user != comment.user and not request.user.is_staff:
        messages.error(request, "You are not authorized to edit this comment.")
        return redirect('manga_detail', manga_id=comment.manga.id)

    if request.method == 'POST':
        comment.content = request.POST.get('content')
        comment.save()
        messages.success(request, "Comment updated successfully.")
        return redirect('manga_detail', manga_id=comment.manga.id)

    return render(request, 'comments/edit_comment.html', {'comment': comment})


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if request.user != comment.user and not request.user.is_staff:
        messages.error(request, "You are not authorized to delete this comment.")
        return redirect('manga_detail', manga_id=comment.manga.id)

    comment.delete()
    messages.success(request, "Comment deleted successfully.")
    return redirect('manga_detail', manga_id=comment.manga.id)


@login_required
def add_comment(request, manga_id):
    manga = get_object_or_404(Manga, id=manga_id)

    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            # Create the new comment and associate it with the manga and user
            Comment.objects.create(user=request.user, manga=manga, content=content)
        return redirect('manga_detail', manga_id=manga.id)

    return redirect('manga_detail', manga_id=manga.id)


def rate_manga(request, manga_id):
    manga = get_object_or_404(Manga, id=manga_id)

    if request.user.is_authenticated:
        if request.method == 'POST':
            rating = request.POST.get('rating')
            if rating:
                # Check if the user has already rated this manga
                existing_rating = Rating.objects.filter(manga=manga, user=request.user).first()
                if existing_rating:
                    existing_rating.rating = rating
                    existing_rating.save()
                else:
                    new_rating = Rating.objects.create(manga=manga, user=request.user, rating=rating)
                return redirect('manga_detail', manga_id=manga.id)

    return redirect('manga_detail', manga_id=manga.id)
