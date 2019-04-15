import requests
from rest_framework import status, viewsets
from rest_framework.response import Response

from restfulmovie.credentials import API_KEY
from .models import Movie, Comment
from .serializers import MovieSerializer, CommentSerializer


class MovieViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing movie instances
    """
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

    def create(self, request):
        title_requested = request.POST['Title']

        params = {'t': title_requested, 'apikey': API_KEY}

        r = requests.get(url='http://www.omdbapi.com/', params=params)

        serializer = MovieSerializer(data=r.json())

        if serializer.is_valid():
            movie = serializer.create(serializer.validated_data)
            movie.save()
            print("Gucci?")
            return Response(serializer.data)

        print(f"Błędy:")
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        instance = Movie.objects.get(pk=pk)

        serializer = MovieSerializer(instance)

        movie = serializer.update(instance, request.POST)

        movie.save()

        return Response(serializer.data)

class CommentViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing comment instances
    """
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def retrieve(self, request, pk=None):
        comments = Comment.objects.filter(movie=pk)
        serializer = CommentSerializer(comments, many=True)

        return Response(serializer.data)
