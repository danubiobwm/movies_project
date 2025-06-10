from pymongo import MongoClient
import os

def sync_movie_to_mongo(movie_id):
    from .models import Movie
    movie = Movie.objects.get(id=movie_id)

    client = MongoClient(os.getenv("MONGO_URI"))
    db = client.movies
    collection = db.movies

    collection.update_one(
        {"tmdb_id": movie.tmdb_id},
        {"$set": {
            "tmdb_id": movie.tmdb_id,
            "title": movie.title,
            "release_date": str(movie.release_date),
            "vote_average": movie.vote_average,
            "popularity": movie.popularity,
            "overview": movie.overview,
            "rating": movie.vote_average,

        }},
        upsert=True
    )
