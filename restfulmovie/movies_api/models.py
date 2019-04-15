from django.db import models

class Movie(models.Model):
    Title = models.CharField(max_length=1500)
    Year = models.CharField(max_length=1500)
    Rated = models.CharField(max_length=1500)
    Released = models.CharField(max_length=1500)
    Runtime = models.CharField(max_length=1500)
    Genre = models.CharField(max_length=1500)
    Director = models.CharField(max_length=1500)
    Writer = models.CharField(max_length=1500)
    Actors = models.CharField(max_length=1500)
    Plot = models.CharField(max_length=1500)
    Language = models.CharField(max_length=1500)
    Country = models.CharField(max_length=1500)
    Awards = models.CharField(max_length=1500)
    Poster = models.CharField(max_length=1500)
    Metascore = models.CharField(max_length=1500)
    imdbRating = models.CharField(max_length=1500)
    imdbVotes = models.CharField(max_length=1500)
    imdbID = models.CharField(max_length=1500)
    Type = models.CharField(max_length=1500)
    DVD = models.CharField(max_length=1500)
    BoxOffice = models.CharField(max_length=1500)
    Production = models.CharField(max_length=1500)
    Website = models.CharField(max_length=1500)
    Response = models.CharField(max_length=1500)

    def __str__(self):
        return f"{self.id}, {self.Title}"

class Rating(models.Model):
    Source = models.CharField(max_length=1500)
    Value = models.CharField(max_length=1500)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='Ratings')

    def __str__(self):
        return f"{self.Source}: {self.Value}"
