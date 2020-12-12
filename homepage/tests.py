from django.test import TestCase

from django.contrib.auth.models import User

"""
    settings.TEST must be True in order to run tests;
    OR, the DB in use must have full permissions.
"""


class HomeUnauthenticatedUser(TestCase):
    def setUp(self):
        self.response = self.client.get('/')

    def test_get(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'homepage/homepage_index.html')

    def test_try_unauthorized_link(self):
        self.response = self.client.get('/profile/')
        self.assertEqual(self.response.status_code, 302)


class HomeAuthenticatedUser(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='Test1', password='s3cr3tp4ssw0rd', email='test@email1.com')
        self.client.login(username='Test1', password='s3cr3tp4ssw0rd')
        self.response = self.client.get('/profile/')

    def test_get(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'users/profile.html')
