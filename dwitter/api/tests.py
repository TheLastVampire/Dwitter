from django.test import TestCase

from .models import Dweet, Dweeter, Comment, Liked, FollowedDweeter
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

# Create your tests here.


class ModelTestCase(TestCase):
    """This class defines the test suite for the models."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.dweet = Dweet(dweeterId=0, text="cute dweet",
                           likeCount=0, crBy=0, lmodDate=0)
        self.dweeter = Dweeter(username="hanazawakana",
                               pswd="abcd", country="japan")
        self.comment = Comment(text="Hommono Tenshi da ne!!")
        self.liked = Liked(likedBy=5)
        self.followed = FollowedDweeter(dweeterId=6)

    def test_model_can_create_a_dweet(self):
        """Test the bucketlist model can create a bucketlist."""
        old_count = Dweet.objects.count()
        self.dweet.save()
        new_count = Dweet.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_model_can_create_a_dweeter(self):
        """Test the bucketlist model can create a bucketlist."""
        old_count = Dweeter.objects.count()
        self.dweeter.save()
        new_count = Dweeter.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_model_can_create_a_comment(self):
        """Test the bucketlist model can create a bucketlist."""
        old_count = Comment.objects.count()
        self.comment.save()
        new_count = Comment.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_model_can_create_a_like(self):
        """Test the bucketlist model can create a bucketlist."""
        old_count = Liked.objects.count()
        self.liked.save()
        new_count = Liked.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_model_can_create_a_follower(self):
        """Test the bucketlist model can create a bucketlist."""
        old_count = FollowedDweeter.objects.count()
        self.followed.save()
        new_count = FollowedDweeter.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.dweeter_data = {'username': 'kanazawa_hana',
                             'pswd': 'seiyuu@1',
                             'fullname': 'Kanazawa Hana',
                             'country': 'Japan'
                             }
        self.response = self.client.post(
            reverse('create'),
            self.dweeter_data,
            format="json")

    def test_api_can_create_a_dweeter(self):
        """Test the api has bucket creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
