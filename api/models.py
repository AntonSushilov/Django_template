from django.db import models

# Create your models here.
class TournamentType(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()

    def __str__(self):
        return self.title


class SportType(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()

    def __str__(self):
        return self.title