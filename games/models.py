from django.db import models


class Game(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    release_date = models.DateField()
    developer = models.ForeignKey('Developer', on_delete=models.SET_NULL, null=True, blank=True)
    genres = models.ManyToManyField('Genre', blank=True)
    platform = models.ManyToManyField('Platform', blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    metacritic_rating = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    cover_image = models.ImageField(upload_to='game_covers/', blank=True, null=True)

    def __str__(self):
        return self.title


class Platform(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Developer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    founded_year = models.PositiveIntegerField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
