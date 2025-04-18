from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    user_score = models.PositiveIntegerField()
    release_date = models.DateField()
    overview = models.TextField()

    def __str__(self):
        return self.title

