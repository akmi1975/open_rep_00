from django.db import models
from smart_selects.db_fields import ChainedForeignKey
# Create your models here.

class Regions(models.Model):
	name = models.CharField(max_length=50, verbose_name='Наименование')

	def __str__(self):
		#return str(self.id) + ' ' + str(self.name)
		return self.name

	class Meta:
		verbose_name_plural = 'Регионы'
		verbose_name = 'Регион'

class GorRayon(models.Model):
	region = models.ForeignKey(Regions, null=True, on_delete=models.PROTECT, verbose_name='Регион')
	#region = models.ManyToManyField(Regions, null=True, verbose_name='Регион')
	name = models.CharField(max_length=50, verbose_name='Наименование')

	def __str__(self):
		#return str(self.region.id) + ' ' + str(self.name)
		return self.name

	class Meta:
		verbose_name_plural = 'Города и(или) Районы'
		verbose_name = 'Город и(или) Район'


class Nsp(models.Model):
	region = models.ForeignKey(Regions, null=True, on_delete=models.PROTECT, verbose_name='Регион')
	#rayon = models.ForeignKey(GorRayon, null=True, on_delete=models.PROTECT, verbose_name='Район')
	rayon = ChainedForeignKey(
        GorRayon,
        chained_field='region',
        chained_model_field='region',
        show_all=False,
        auto_choose=True,
        null=True,
        verbose_name='Район')	
	name = models.CharField(max_length=50, verbose_name='Наименование')
	mo = models.BooleanField(verbose_name='Муниципальное образование')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Населенные пункты'
		verbose_name = 'Населеный пункт'

class Otrasl(models.Model):
	name = models.CharField(max_length=50, verbose_name='Наименование')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Отрасли'
		verbose_name = 'Отрасль'

class PodOtrasl(models.Model):
	otrasl = models.ForeignKey(Otrasl, null=True, on_delete=models.PROTECT, verbose_name='Отрасль')
	name = models.CharField(max_length=50, verbose_name='Наименование')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Подотрасли'
		verbose_name = 'Подотрасль'
