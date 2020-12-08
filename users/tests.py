from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile


class TestProfileCreation(TestCase):
    def setUp(self):
        username = 'Test1'
        email = 'test@email.com'
        password1 = 'asdf1234qwer'
        testuser = User(
            username=username,
            email=email,
            password=password1,
        )
        testuser.save()

    def test_Profile_auto_creation_with_user_registration(self):
        setup_user = User.objects.all()[0]
        query_profiles = Profile.objects.all()
        self.assertTrue(query_profiles is not None)
        self.assertTrue(query_profiles[0].user_id == setup_user.id)
        self.assertTrue(query_profiles[0].user)
        self.assertTrue(query_profiles[0].clean_quote_of_the_day is False)
        self.assertTrue(query_profiles[0].image == '/profile/default.jpg')

