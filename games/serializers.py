from rest_framework import serializers
from .models import Game, Developer


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['title', 'description', 'release_date', 'developer', 'genres', 'platform', 'rating',
                  'metacritic_rating', 'cover_image']


class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = ['name', 'location', 'founded_year', 'website']
