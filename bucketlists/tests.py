from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Bucketlist

class BucketlistModelTestCase(TestCase):
    """This class defines the test suite for the bucketlist model"""

    def setUp(self):
        user = User.objects.create(username="CuppyCake")
        self.bucketlist_name = "Have no regrets"
        self.bucketlist = Bucketlist(name=self.bucketlist_name, owner=user)

    def test_model_can_create_bucketlist(self):
        """Test bucketlist model can create a bucketlist"""
        old_count = Bucketlist.objects.count()
        self.bucketlist.save()
        new_count = Bucketlist.objects.count()
        self.assertNotEqual(old_count, new_count)


class BucketlistViewTestCase(TestCase):
    """Test suite for bucketlist api views"""

    def setUp(self):
        user = User.objects.create(username="CuppyCake")
        self.client = APIClient()
        self.client.force_authenticate(user=user)
        self.bucketlist_data = {'name': 'Have no regrets', 'owner': user.id}
        self.response = self.client.post(
            reverse('bucketlists:create'),
            self.bucketlist_data,
            format="json"
        )

    def test_view_can_create_bucketlist(self):
        """Test the api can create a bucketlist"""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_authorization_enforced(self):
        """Test the api has authorization"""
        new_user = User.objects.create(username="newguy")
        new_client = APIClient()
        new_client.force_authenticate(user=new_user)
        reponse = new_client.get(
            reverse('bucketlists:details',
                    kwargs={'pk': 2}),
            format="json"
        )
        self.assertEqual(reponse.status_code, status.HTTP_403_FORBIDDEN)

    def test_view_can_get_bucketlist(self):
        """Test the api can retrieve a bucketlist"""
        bucketlist = Bucketlist.objects.get()
        response = self.client.get(
            reverse('bucketlists:details',
                    kwargs={'pk': bucketlist.id}),
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, bucketlist)

    def test_view_can_update_bucketlist(self):
        """Test the api can update a bucketlist"""
        bucketlist = Bucketlist.objects.get()
        change_bucketlist = {'name': 'new_test_name'}
        response = self.client.put(
            reverse('bucketlists:details',
                    kwargs={'pk': bucketlist.id}),
            change_bucketlist,
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_view_can_delete_bucketlist(self):
        """Test the api can delete a bucketlist"""
        bucketlist = Bucketlist.objects.get()
        response = self.client.delete(
            reverse('bucketlists:details',
                    kwargs={'pk': bucketlist.id}),
            format="json",
            follow=True
        )

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

