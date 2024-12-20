from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages


class UserAccountTests(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='password1235')
        self.user_profile = self.user.profile  # Assuming the user has a related profile

    def test_register_view(self):
        url = reverse('register')
        data = {
            'username': 'newuser',
            'password1': 'newpassword123',
            'password2': 'newpassword123',
        }
        response = self.client.post(url, data)

        # Check if user is created and redirected to the profile page
        self.assertRedirects(response, reverse('profile'))
        self.assertTrue(User.objects.filter(username='newuser').exists())

        # Check if a success message is displayed
        messages = [msg.message for msg in get_messages(response.wsgi_request)]
        self.assertIn('Account created for newuser!', messages)

    def test_profile_view(self):
        self.client.login(username='testuser', password='password1235')
        url = reverse('profile')
        response = self.client.get(url)

        # Check if the profile page is rendered successfully
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'testuser')  # Check if the username is in the profile page

    def test_delete_account_view(self):
        self.client.login(username='testuser', password='password1235')
        url = reverse('delete_account')
        response = self.client.post(url)

        # Check if the account is deleted and redirected to the home page
        self.assertRedirects(response, reverse('home'))
        self.assertFalse(User.objects.filter(username='testuser').exists())

        # Check if a success message is displayed
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

        # Check if the password is reset successfully
        self.assertRedirects(response, reverse('password_reset_complete'))
        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password('newpassword1235'))

        # Check if a success message is displayed
        messages = [msg.message for msg in get_messages(response.wsgi_request)]
        self.assertIn('Password reset successfully', messages)

    def test_password_reset_invalid_user(self):
        url = reverse('password_reset_confirm', kwargs={'user_id': 999})  # Invalid user ID
        response = self.client.get(url)

        # Check if 404 error is raised for invalid user
        self.assertEqual(response.status_code, 404)


class ProfileUpdateTest(TestCase):

    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client.login(username='testuser', password='password123')

    def test_update_username(self):
        # The URL for the update profile view
        url = reverse('update_profile')

        # Data with a new username
        data = {
            'user': self.user,  # keeping the user as part of the form is optional, depending on how you handle the form in your view
            'username': 'testuser',  # the new username for the test
        }

        # Post the data to the update profile form
        response = self.client.post(url, data)

        # Retrieve the user object from the database after the update
        updated_user = User.objects.get(id=self.user.id)

        # Check if the username has been updated
        self.assertEqual(updated_user.username, 'testuser')

    def tearDown(self):
        self.user.delete()
