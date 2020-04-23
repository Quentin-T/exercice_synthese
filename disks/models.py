from django.db import models


# Create your models here.

class artist(models.Model):
    Name = models.CharField(max_length=120)

    def __str__(self):
        return self.Name


class album(models.Model):
    Title = models.CharField(max_length=160)
    artist = models.ForeignKey('artist', on_delete=models.CASCADE)

    class Meta:
        ordering = ['artist']

    def __str__(self):
        return self.Title


class track(models.Model):
    Name = models.CharField(max_length=200)
    Composer = models.CharField(max_length=220)
    Milliseconds = models.TextField()
    Bytes = models.IntegerField()
    UnitPrice = models.DecimalField(max_digits=10, decimal_places=2)
    album = models.ForeignKey('album', on_delete=models.CASCADE)

    def __str__(self):
        return self.Name
