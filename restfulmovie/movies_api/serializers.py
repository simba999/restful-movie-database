from rest_framework import serializers
from .models import Movie, Rating, Comment

class RatingsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        exclude = ('movie',)

class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):

    Ratings = RatingsSerializer(many=True)
    Comments = CommentSerializer(many=True)

    class Meta:
        model = Movie
        fields = '__all__'
        depth = 1

    def create(self, validated_data):
        validated_data = validated_data.copy()
        ratings_data = validated_data.pop('Ratings')
        movie = Movie.objects.create(**validated_data)
        for rating_data in ratings_data:
            Rating.objects.create(movie=movie, **rating_data)

        return movie

    def update(self, instance, validated_data):
        validated_data = validated_data.copy()

        for key, value in validated_data.items():
            setattr(instance, key, value)

        return instance
