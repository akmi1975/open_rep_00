from django.db import models
from smart_selects.db_fields import ChainedForeignKey, ChainedManyToManyField
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
	mo = models.BooleanField(null=True, verbose_name='Муниципальное образование')

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

class Org(models.Model):
	#rayon = models.ForeignKey(GorRayon, null=True, on_delete=models.PROTECT, verbose_name='Район')
	otrasl = models.ForeignKey(Otrasl, null=True, on_delete=models.PROTECT, verbose_name='Отрасль')
	pod_otrasl = ChainedForeignKey(
        PodOtrasl,
        chained_field='otrasl',
        chained_model_field='otrasl',
        show_all=False,
        auto_choose=True,
        null=True,
        verbose_name='Подотрасль')
	region = models.ForeignKey(Regions, null=True, on_delete=models.PROTECT, verbose_name='Регион')
	rayon = ChainedForeignKey(
        GorRayon,
        chained_field='region',
        chained_model_field='region',
        show_all=False,
        auto_choose=True,
        null=True,
        verbose_name='Район')
	nsp = ChainedForeignKey(
        Nsp,
        chained_field='rayon',
        chained_model_field='rayon',
        show_all=False,
        auto_choose=True,
        null=True,
        verbose_name='Населенный пункт')
	inn = models.CharField(max_length=12, verbose_name='ИНН')
	name = models.CharField(max_length=300, verbose_name='Наименование')
	name_short = models.CharField(null=True, max_length=300, verbose_name='Сокращенное наименование')
	okved = models.CharField(null=True, max_length=8, verbose_name='ОКВЭД')
	okved_name = models.CharField(null=True, max_length=500, verbose_name='ОКВЭД наименование')

	def __str__(self):
		return self.name_short

	class Meta:
		verbose_name_plural = 'Организации'
		verbose_name = 'Организация'

class orgContact(models.Model):
	org = models.ForeignKey(Org, null=True, on_delete=models.PROTECT, verbose_name='Организация')
	adres = models.CharField(null=True, blank=True, max_length=200, verbose_name='Адрес')
	telefone = models.CharField(null=True, blank=True, max_length=50, verbose_name='Телефоны')
	email = models.CharField(null=True, blank=True, max_length=50, verbose_name='e-mail')
	url = models.CharField(null=True, blank=True, max_length=50, verbose_name='Интрнет адрес')
	vremya = models.CharField(null=True, blank=True, max_length=50, verbose_name='Время работы')

	class Meta:
		verbose_name_plural = 'Контактная информация'
		verbose_name = 'Контактная информация'

