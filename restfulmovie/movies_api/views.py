from rest_framework import viewsets
from .models import Movie
from .serializers import MovieSerializer

class MovieViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing movie instances
    """
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
