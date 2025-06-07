from celery import shared_task
import requests
from .models import Movie
from django.conf import settings

@shared_task
def fetch_movies():
    url = f"https://api.themoviedb.org/3/movie/popular?api_key={settings.TMDB_API_KEY}&language=en-US&page=1"
    response = requests.get(url)
    if response.status_code == 200:
        for item in response.json().get('results', []):
            Movie.objects.update_or_create(
                tmdb_id=item['id'],
                defaults={
                    'title': item['title'],
                    'release_date': item['release_date'],
                    'vote_average': item['vote_average'],
                    'popularity': item['popularity'],
                    'overview': item['overview'],
                    'is_custom': False,
                }
            )
