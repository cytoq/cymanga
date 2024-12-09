from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Root URL for both logged-in and public users
    path('manga/', views.MangaListView.as_view(), name='manga_list'),  # Authenticated users see the list here
    path('manga/add/', views.MangaCreateView.as_view(), name='manga_create'),
    path('manga/<int:pk>/edit/', views.MangaUpdateView.as_view(), name='manga_update'),
    path('manga/<int:pk>/delete/', views.MangaDeleteView.as_view(), name='manga_delete'),
    path('manga/<int:pk>/', views.MangaDetailView.as_view(), name='manga_detail'),
]