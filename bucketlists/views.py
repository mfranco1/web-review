from rest_framework import generics
from .serializers import BucketlistSerializer
from .models import Bucketlist

class BucketlistCreateView(generics.ListCreateAPIView):
    """Defines the create behavior of the bucketlist api"""
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer

    def perform_create(self, serializer):
        """Create and save new bucketlist from post data"""
        serializer.save()

class BucketlistDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """Defines the http GET, PUT, DELETE requests"""
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
