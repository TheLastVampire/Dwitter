from django.shortcuts import render

from rest_framework import generics
from .serializers import DweeterSerializer
from .models import Dweet, Dweeter, Comment, Liked, FollowedDweeter


# Create your views here.
class CreateDweeterView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Dweeter.objects.all()
    serializer_class = DweeterSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()
