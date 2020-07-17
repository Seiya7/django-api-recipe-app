from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@gemail.com'
        password = 'Password'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
            )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test that email for new user is normalized"""
        email = 'test@EMAIL.COM'
        user = get_user_model().objects.create_user(email, 'passWD')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Raise error when creating user with no email"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'passWD')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@email.com', 'passWD')

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)