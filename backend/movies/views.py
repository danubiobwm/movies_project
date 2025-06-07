from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Movie
from .serializers import MovieSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {
        "vote_average": ["gte"],
        "release_date": ["gte", "lte"],
    }
    search_fields = ["title", "overview"]
    ordering_fields = ["title", "popularity", "release_date"]
