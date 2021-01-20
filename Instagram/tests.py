from django.test import TestCase
from .models import Profile, Image
from django.contrib.auth.models import User


class TestProfile(TestCase):
    def setUp(self):
        self.user = User(user='preston')
        self.user.save()

        self.profileTest = Profile(id=1, pro_pic='test.jpg', Bio='test profile',
                                    user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.profileTest, Profile))

    def test_save_profile(self):
        self.profileTest.save_profile()
        pp = Profile.objects.all()
        self.assertTrue(len(pp) > 0)


class TestImage(TestCase):
    def setUp(self):
        self.profileTest = Profile(user=User(user='test'))
        self.profileTest.save()

        self.imageTest = Image(image='default.png', name='test', caption='default test', user=self.profile_test)

    def test_instance(self):
        self.assertTrue(isinstance(self.imageTest, Image))

    def test_save_image(self):
        self.imageTest.savePost()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_image(self):
        self.imageTest.delete_image()
        pp = Profile.objects.all()
        self.assertTrue(len(pp) < 1)