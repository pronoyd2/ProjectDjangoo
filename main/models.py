from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length= 300)
    director = models.CharField(max_length= 300)
    cast = models.CharField(max_length= 300)
    description = models.TextField(max_length= 5000, null = True)
    date = models.DateField(null = True)
    averagerating = models.FloatField(null = True)
    image = models.URLField(default= None, null= True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete= CASCADE)
    user = models.ForeignKey(User, on_delete= CASCADE )
    comment = models.TextField(max_length= 1000)
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.user.username


