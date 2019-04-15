import requests
from django.db.models import Count
from rest_framework import status, viewsets, views
from rest_framework.response import Response
import datetime

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
        try:
            title_requested = request.POST['Title']
        except KeyError:
            return Response("Title not provided. Did you remember to capitalize first letter?",
                            status.HTTP_400_BAD_REQUEST)

        params = {'t': title_requested, 'apikey': API_KEY}

        r = requests.get(url='http://www.omdbapi.com/', params=params)

        serializer = MovieSerializer(data=r.json())

        if serializer.is_valid():
            movie = serializer.create(serializer.validated_data)
            movie.save()

            return Response(serializer.data)

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

class TopView(views.APIView):
    """
    A viewset for obtaining top movies
    """
    def get(self, request):
        params_from = [int(param) for param in request.GET['date_from'].split('.')]
        params_to = [int(param) for param in request.GET['date_to'].split('.')]

        date_from = datetime.date(params_from[0], params_from[1], params_from[2])
        date_to = datetime.date(params_to[0], params_to[1], params_to[2])

        queryset = Comment.objects.values('movie')\
                    .annotate(comment_count=Count('movie'))\
                    .filter(date__gte=date_from)\
                    .filter(date__lte=date_to)\
                    .order_by('-comment_count')

        ranking = \
        [
            {
                "movie_id": movie['movie'],
                "total_comments": movie['comment_count'],
            } \
            for movie \
            in queryset.iterator()
        ]

        last_number = 0
        counter = 0
        for movie in ranking:
            if movie["total_comments"] != last_number:
                counter += 1
                last_number = movie["total_comments"]

            movie["rank"] = counter

        return Response(ranking)
