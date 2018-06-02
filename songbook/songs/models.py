from django.db import models

# Create your models here.
class Song(models.Model):
    image = models.CharField(max_length=10000)
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    link = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    #"/songs/%i/" % self.id
    def get_absolute_url(self):
        return "/songs/"
