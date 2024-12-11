import requests
from django.core.management.base import BaseCommand
from django.core.files import File
from io import BytesIO
from manga.models import Manga


class Command(BaseCommand):
    help = 'Import mangas from Jikan API and populate the database'

    def handle(self, *args, **kwargs):
        # URL for the Jikan API (MyAnimeList API)
        url = "https://api.jikan.moe/v4/manga"

        # Fetch the data (you can modify this to filter or paginate as needed)
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            mangas = data.get('data', [])

            for manga in mangas:
                # Extract the data you want from the API response
                title = manga.get('title')
                author = manga.get('authors', [{}])[0].get('name', 'Unknown')
                genre = manga.get('genres', [{}])[0].get('name', 'Unknown')
                status = manga.get('status', 'ongoing')
                total_chapters = manga.get('chapters', None)
                start_date = manga.get('start_date', None)
                end_date = manga.get('end_date', None)
                cover_image_url = manga.get('images', {}).get('jpg', {}).get('large_image_url', None)

                # Download the cover image if it exists
                cover_image = None
                if cover_image_url:
                    img_data = requests.get(cover_image_url).content
                    img_file = BytesIO(img_data)
                    cover_image_name = f"{title}_cover.jpg"  # Generate a filename for the cover image
                    cover_image = File(img_file, name=cover_image_name)

                # Create or update the manga entry in the database
                manga_entry = Manga.objects.create(
                    title=title,
                    author=author,
                    genre=genre,
                    status=status,
                    total_chapters=total_chapters,
                    start_date=start_date,
                    end_date=end_date,
                    cover_image=cover_image  # Store the image with a filename
                )
                self.stdout.write(self.style.SUCCESS(f'Successfully added manga: {title}'))
        else:
            self.stdout.write(self.style.ERROR('Failed to retrieve data from API'))
