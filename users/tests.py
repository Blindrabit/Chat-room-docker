from django.test import TestCase
from django.contrib.auth import get_user_model

class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='test',
            email='testuser@email.com',
            password='testpassword123',
        )
        self.assertEqual(user.username, 'test')
        self.assertEqual(user.email, 'testuser@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username='admintest',
            email='admintestuser@email.com',
            password='testpassword123',
        )
        self.assertEqual(user.username, 'admintest')
        self.assertEqual(user.email, 'admintestuser@email.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

# Create your tests here.
