from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Movie
from .tasks import sync_movie_to_mongo
from pymongo import MongoClient
import os

@receiver(post_save, sender=Movie)
def sync_on_save(sender, instance, **kwargs):
    sync_movie_to_mongo(instance.id)

@receiver(post_delete, sender=Movie)
def sync_on_delete(sender, instance, **kwargs):
    client = MongoClient(os.getenv("MONGO_URI"))
    db = client.movies
    db.movies.delete_one({"tmdb_id": instance.tmdb_id})
