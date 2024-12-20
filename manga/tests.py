from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from .models import Manga, Comment, Rating


class MangaModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='TestPassword123!')
        self.manga = Manga.objects.create(
            title="Test Manga",
            author="Test Author",
            genre="Action",
            status="Publishing",
            total_chapters=10,
            cover_image=None
        )

    def test_manga_str(self):
        self.assertEqual(str(self.manga), "Test Manga")

    def test_average_rating_no_ratings(self):
        self.assertIsNone(self.manga.average_rating())

    def test_average_rating_with_ratings(self):
        Rating.objects.create(manga=self.manga, user=self.user, rating=5)
        Rating.objects.create(manga=self.manga, user=self.user, rating=4)
        self.assertEqual(self.manga.average_rating(), 4.5)


class CommentModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='TestPassword123!')
        self.manga = Manga.objects.create(
            title="Test Manga",
            author="Test Author",
            genre="Action",
            status="Publishing",
            total_chapters=10,
            cover_image=None
        )
        self.comment = Comment.objects.create(
            user=self.user,
            manga=self.manga,
            content="Great manga!"
        )

    def test_comment_str(self):
        self.assertEqual(str(self.comment), "Comment by testuser on Test Manga")


class RatingModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='TestPassword123!')
        self.manga = Manga.objects.create(
            title="Test Manga",
            author="Test Author",
            genre="Action",
            status="Publishing",
            total_chapters=10,
            cover_image=None
        )
        self.rating = Rating.objects.create(
            manga=self.manga,
            user=self.user,
            rating=4
        )

    def test_rating_str(self):
        self.assertEqual(str(self.rating), "testuser rated Test Manga 4/5")


class MangaViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='TestPassword123!')
        self.manga = Manga.objects.create(
            title="Test Manga",
            author="Test Author",
            genre="Action",
            status="Publishing",
            total_chapters=10,
            cover_image=None
        )

    def test_manga_list_view(self):
        response = self.client.get(reverse('manga_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Manga")

    def test_manga_delete_view(self):
        self.client.login(username='testuser', password='TestPassword123!')
        response = self.client.get(reverse('manga_delete', args=[self.manga.id]))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(reverse('manga_delete', args=[self.manga.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Manga.objects.count(), 0)


class CommentViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='TestPassword123!')
        self.manga = Manga.objects.create(
            title="Test Manga",
            author="Test Author",
            genre="Action",
            status="Publishing",
            total_chapters=10,
            cover_image=None
        )

    def test_add_comment_view(self):
        self.client.login(username='testuser', password='TestPassword123!')
        data = {'content': 'This is a comment.'}
        response = self.client.post(reverse('add_comment', args=[self.manga.id]), data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.manga.comments.count(), 1)

    def test_edit_comment_view(self):
        self.client.login(username='testuser', password='TestPassword123!')
        comment = Comment.objects.create(
            user=self.user,
            manga=self.manga,
            content="Original comment"
        )
        data = {'content': 'Updated comment'}
        response = self.client.post(reverse('edit_comment', args=[comment.id]), data)
        self.assertEqual(response.status_code, 302)
        comment.refresh_from_db()
        self.assertEqual(comment.content, 'Updated comment')


class RatingViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='TestPassword123!')
        self.manga = Manga.objects.create(
            title="Test Manga",
            author="Test Author",
            genre="Action",
            status="Publishing",
            total_chapters=10,
            cover_image=None
        )

    def test_rate_manga_view(self):
        self.client.login(username='testuser', password='TestPassword123!')
        data = {'rating': 4}
        response = self.client.post(reverse('rate_manga', args=[self.manga.id]), data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.manga.ratings.count(), 1)
