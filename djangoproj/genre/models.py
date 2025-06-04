from django.db import models

class Collection(models.Model):
    collection_name = models.CharField(max_length = 100)
    description = models.CharField(max_length= 500)
    collectionCover = models.CharField(max_length=1000)

    def __str__(self):
        return self.collection_name

class Piece(models.Model):
    collection = models.ForeignKey(Collection, on_delete= models.CASCADE)
    title = models.CharField(max_length=100)
    type = models.CharField(max_length= 100)
    artist = models.CharField( max_length=100)
    year = models.IntegerField()
    pieceCover = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.title} by {self.artist} ({self.year})"