from django.db import models

class Movie(models.Model):
    tmdb_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    vote_average = models.FloatField()
    popularity = models.FloatField()
    overview = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_custom = models.BooleanField(default=False)

    def __str__(self):
        return self.title