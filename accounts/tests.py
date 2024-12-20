from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages


class UserAccountTests(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='password1235')
        self.user_profile = self.user.profile

    def test_register_view(self):
        url = reverse('register')
        data = {
            'username': 'newuser',
            'password1': 'newpassword123',
            'password2': 'newpassword123',
        }
        response = self.client.post(url, data)

        self.assertRedirects(response, reverse('profile'))
        self.assertTrue(User.objects.filter(username='newuser').exists())

        messages = [msg.message for msg in get_messages(response.wsgi_request)]
        self.assertIn('Account created for newuser!', messages)

    def test_profile_view(self):
        self.client.login(username='testuser', password='password1235')
        url = reverse('profile')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'testuser')

    def test_delete_account_view(self):
        self.client.login(username='testuser', password='password1235')
        url = reverse('delete_account')
        response = self.client.post(url)

        self.assertRedirects(response, reverse('home'))
        self.assertFalse(User.objects.filter(username='testuser').exists())

        messages = [msg.message for msg in get_messages(response.wsgi_request)]
        self.assertIn('Your account has been deleted.', messages)

    def test_password_reset_view(self):
        url = reverse('password_reset')
        data = {
            'old_password': 'password1235',
            'new_password1': 'newpassword1235',
            'new_password2': 'newpassword1235',
        }
        self.client.login(username='testuser', password='password1235')
        response = self.client.post(url, data)

        self.assertRedirects(response, reverse('password_reset_complete'))
        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password('newpassword1235'))

        messages = [msg.message for msg in get_messages(response.wsgi_request)]
        self.assertIn('Password reset successfully', messages)


class ProfileUpdateTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client.login(username='testuser', password='password123')

    def test_update_username(self):
        url = reverse('update_profile')

        data = {
            'user': self.user,
            'username': 'testuser',
        }

        response = self.client.post(url, data)

        updated_user = User.objects.get(id=self.user.id)

        self.assertEqual(updated_user.username, 'testuser')

    def tearDown(self):
        self.user.delete()
