from django.db import models

# Create your models here.

class Sport(models.Model):
    name = models.CharField(max_length=255)
    key = models.CharField(max_length=255,default='key')

    def __str__(self):
        return self.name


class Wager(models.Model):
    name = models.CharField(max_length=255)
    event = models.CharField(max_length=255)
    stake = models.IntegerField()
    sport = models.ForeignKey(Sport, related_name='wagers', on_delete=models.CASCADE)
    odds =  models.FloatField()
    image = models.ImageField(upload_to='wager_images', blank=True, null=True)


    def __str__(self):
        return self.name