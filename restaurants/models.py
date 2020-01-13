from django.db import models

# Create your models here.
class Restaurant(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	opening_time = models.TimeField()
	closing_time = models.TimeField()