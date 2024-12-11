from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Manga


class MangaListViewTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.manga1 = Manga.objects.create(title="Manga One", author="Author One")
        self.manga2 = Manga.objects.create(title="Manga Two", author="Author Two")
        self.client.login(username='testuser', password='testpassword')

    def test_manga_list_get(self):
        response = self.client.get(reverse('manga_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'manga/index.html')
        self.assertContains(response, 'Manga One')
        self.assertContains(response, 'Manga Two')

    def test_search_functionality(self):
        response = self.client.get(reverse('manga_list'), {'query': 'Manga One'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Manga One')
        self.assertNotContains(response, 'Manga Two')



class AddMangaViewTest(TestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='password')

        # Define common test data
        self.manga_data = {
            'title': 'New Manga',
            'author': 'New Author',
            'genre': 'Action',
            'status': 'Publishing',
            'chapters_read': 0,
            'total_chapters': 10,
        }

        # Log the user in
        self.client.login(username='testuser', password='password')

    def test_add_manga_view_redirects_successfully(self):
        """Test that submitting valid manga data redirects to the manga list."""
        response = self.client.post(reverse('add_manga'), self.manga_data)
        self.assertRedirects(response, reverse('manga_list'))

    def test_add_manga_creates_database_entry(self):
        """Test that submitting valid manga data creates the correct database entry."""
        self.client.post(reverse('add_manga'), self.manga_data)

        # Verify database state
        self.assertEqual(Manga.objects.count(), 1)
        created_manga = Manga.objects.first()
        self.assertEqual(created_manga.title, 'New Manga')
        self.assertEqual(created_manga.author, 'New Author')
        self.assertEqual(created_manga.genre, 'Action')


