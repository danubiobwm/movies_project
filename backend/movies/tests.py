from django.test import TestCase
from .models import Movie
from rest_framework.test import APIClient

class MovieModelTest(TestCase):
    def test_create_movie(self):
        movie = Movie.objects.create(
            tmdb_id=1,
            title="Exemplo",
            release_date="2020-01-01",
            vote_average=8.5,
            popularity=100,
            overview="Um filme de exemplo",
            is_custom=True
        )
        self.assertEqual(movie.title, "Exemplo")

class MovieAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_movie_via_api(self):
        response = self.client.post("/api/movies/", {
            "tmdb_id": 2,
            "title": "Novo Filme",
            "release_date": "2021-01-01",
            "vote_average": 7.5,
            "popularity": 80,
            "overview": "Sinopse...",
            "is_custom": True
        }, format='json')
        self.assertEqual(response.status_code, 201)