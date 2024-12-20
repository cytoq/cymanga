from django.urls import path
from .views import CreateMangaView, UpdateMangaView, MangaListView, MangaDeleteView, manga_detail, delete_comment, edit_comment, add_comment, rate_manga

urlpatterns = [
    path('mangas/', MangaListView.as_view(), name='manga_list'),
    path('mangas/add/', CreateMangaView.as_view(), name='add_manga'),
    path('mangas/<int:pk>/edit/', UpdateMangaView.as_view(), name='manga_edit'),
    path('mangas/<int:pk>/delete/', MangaDeleteView.as_view(), name='manga_delete'),
    path('mangas/manga/<int:manga_id>/', manga_detail, name='manga_detail'),
    path('comment/edit/<int:comment_id>/', edit_comment, name='edit_comment'),
    path('comment/delete/<int:comment_id>/', delete_comment, name='delete_comment'),
    path('mangas/<int:manga_id>/comment/add/', add_comment, name='add_comment'),
    path('mangas/<int:manga_id>/rate/', rate_manga, name='rate_manga'),
]
