from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('manga.urls')),  # Include the `manga` app's URLs for the root path
]