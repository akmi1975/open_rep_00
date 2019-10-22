from django.db import models

# Create your models here.

class Regions(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name	

class GorRayon(models.Model):
	region = models.ForeignKey(Regions, null=True, on_delete=models.PROTECT)
	name = models.CharField(max_length=50)