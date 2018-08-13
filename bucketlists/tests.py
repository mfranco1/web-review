from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse
from django.test import TestCase
from .models import Bucketlist

class BucketlistModelTestCase(TestCase):
    """This class defines the test suite for the bucketlist model"""

    def setUp(self):
        self.bucketlist_name = "Sevatar"
        self.bucketlist = Bucketlist(name=self.bucketlist_name)

    def test_model_can_create_bucketlist(self):
        """Test bucketlist model can create a bucketlist"""
        old_count = Bucketlist.objects.count()
        self.bucketlist.save()
        new_count = Bucketlist.objects.count()
        self.assertNotEqual(old_count, new_count)


class BucketlistViewTestCase(TestCase):
    """Test suite for bucketlist api views"""

    def setUp(self):
        self.client = APIClient()
        self.bucketlist_data = {'name': 'Have no regrets'}
        self.response = self.client.post(
            reverse('create'),
            self.bucketlist_data,
            format="json"
        )

    def test_view_can_create_bucketlist(self):
        """Test the api can create a bucketlist"""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
