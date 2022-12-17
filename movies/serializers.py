from rest_framework import serializers
from .models import RateMovie
from users.serializers import RegisterSerializer
from .models import Movie, MovieOrder

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, allow_null=True, default=None)
    rating = serializers.ChoiceField(
        allow_null=True,
        choices=RateMovie.choices,
        default=RateMovie.G
        )
    synopsis = serializers.CharField(allow_null=True, default=None)
    added_by = serializers.SerializerMethodField("get_added_by")
    def get_added_by(self, obj: Movie):
        return obj.user.email
    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.SerializerMethodField("get_title")
    buyed_at = serializers.DateTimeField(read_only=True)
    buyed_by = serializers.SerializerMethodField("get_buyed_by")
    price = serializers.DecimalField(max_digits=8, decimal_places=2)

    def get_title(self, obj: MovieOrder) -> str:
        return obj.movie.title
    def get_buyed_by(self, obj: MovieOrder) -> str:
        return obj.user.email
    def create(self, validated_data):

        return  MovieOrder.objects.create(**validated_data)

