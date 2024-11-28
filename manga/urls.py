from django.urls import path
from . import views
from .views import MangaListView, MangaCreateView, MangaUpdateView, MangaDeleteView, MangaDetailView


urlpatterns = [
    path('', views.index, name='index'),
    path('', MangaListView.as_view(), name='index'),
    path('manga/add/', MangaCreateView.as_view(), name='manga_create'),
    path('manga/<int:pk>/edit/', MangaUpdateView.as_view(), name='manga_update'),
path('manga/<int:pk>/delete/', MangaDeleteView.as_view(), name='manga_delete'),
path('manga/<int:pk>/', MangaDetailView.as_view(), name='manga_detail'),
]
