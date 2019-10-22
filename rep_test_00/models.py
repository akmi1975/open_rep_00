from django.db import models

# Create your models here.

class Regions(models.Model):
	name = models.CharField(max_length=50, verbose_name='Наименование')

	def __str__(self):
		return self.name	

	class Meta:
		verbose_name_plural = 'Регионы'
		verbose_name = 'Регион'

class GorRayon(models.Model):
	region = models.ForeignKey(Regions, null=True, on_delete=models.PROTECT, verbose_name='Регион')
	name = models.CharField(max_length=50, verbose_name='Наименование')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Города и(или) Районы'
		verbose_name = 'Город и(или) Район'


class Nsp(models.Model):
	region = models.ForeignKey(Regions, null=True, on_delete=models.PROTECT, verbose_name='Регион')
	rayon = models.ForeignKey(GorRayon, null=True, on_delete=models.PROTECT, verbose_name='Район')
	name = models.CharField(max_length=50, verbose_name='Наименование')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Населенные пункты'
		verbose_name = 'Населеный пункт'

