import requests
from rest_framework import status, viewsets
from rest_framework.response import Response

from restfulmovie.credentials import API_KEY
from .models import Movie
from .serializers import MovieSerializer


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
