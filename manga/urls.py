from django.urls import path
from .views import MangaListView, AddMangaView, MangaUpdateView, MangaDeleteView, MangaDetailView, delete_comment, edit_comment, add_comment, rate_manga


urlpatterns = [
    path('mangas/', MangaListView.as_view(), name='manga_list'),
    path('mangas/add/', AddMangaView.as_view(), name='add_manga'),
    path('mangas/<int:pk>/edit/', MangaUpdateView.as_view(), name='manga_edit'),
    path('mangas/<int:pk>/delete/', MangaDeleteView.as_view(), name='manga_delete'),
    path('manga/<int:pk>/', MangaDetailView.as_view(), name='manga_detail'),
    path('comment/edit/<int:comment_id>/', edit_comment, name='edit_comment'),
    path('comment/delete/<int:comment_id>/', delete_comment, name='delete_comment'),
    path('mangas/<int:manga_id>/comment/add/', add_comment, name='add_comment'),
    path('mangas/<int:manga_id>/rate/', rate_manga, name='rate_manga'),
]
