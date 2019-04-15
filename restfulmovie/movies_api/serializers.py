from rest_framework import serializers
from .models import Movie, Rating

class RatingsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        exclude = ('movie',)

class MovieSerializer(serializers.ModelSerializer):

    Ratings = RatingsSerializer(many=True)

    class Meta:
        model = Movie
        fields = '__all__'
        depth = 1
        