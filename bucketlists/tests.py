from django.test import TestCase
from .models import Bucketlist

class BucketlistTestCase(TestCase):
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
