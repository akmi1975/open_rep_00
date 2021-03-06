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

class CatUslugi(models.Model):
	name = models.CharField(max_length=50, verbose_name='Наименование категории')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Категории услуг'
		verbose_name = 'Категория услуг'


class VidUslugi(models.Model):
	cat_usl = models.ForeignKey(CatUslugi, null=True, on_delete=models.PROTECT, verbose_name='Категория услуги')
	name = models.CharField(max_length=50, verbose_name='Наименование вида')
	pod_otr_txt = models.CharField(max_length=50, null=True, blank=True, verbose_name='Подотрасли (через запятую)')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Виды услуг'
		verbose_name = 'Вид услуги'


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
	inn = models.CharField(max_length=12, null=True, blank=True, verbose_name='ИНН')
	name = models.CharField(max_length=300, verbose_name='Наименование')
	name_short = models.CharField(null=True, max_length=300, verbose_name='Сокращенное наименование')
	okved = models.CharField(null=True, blank=True, max_length=8, verbose_name='ОКВЭД')
	okved_name = models.CharField(null=True, blank=True, max_length=500, verbose_name='ОКВЭД наименование')

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

class Sheff(models.Model):
	org = models.ForeignKey(Org, null=True, on_delete=models.PROTECT, verbose_name='Организация')
	fm = models.CharField(null=True, blank=True, max_length=50, verbose_name='Фамилия')
	im = models.CharField(null=True, blank=True, max_length=50, verbose_name='Имя')
	ot = models.CharField(null=True, blank=True, max_length=50, verbose_name='Отчество')
	dolzhn = models.CharField(null=True, blank=True, max_length=50, verbose_name='Должность')
	inn_ruk = models.CharField(null=True, blank=True, max_length=12, verbose_name='ИНН руководителя')
	doc = models.CharField(null=True, blank=True, max_length=20, verbose_name='Документ')
	# документ на основаниии чего он утвержден руководителем
	nom_doc = models.CharField(null=True, blank=True, max_length=10, verbose_name='Номер документа')
	dt_doc = models.CharField(null=True, blank=True, max_length=10, verbose_name='Дата документа')
	active = models.BooleanField(verbose_name='Действующий', null=True)

	def __str__(self):
		return f'{self.fm} {self.im} {self.ot}'

	class Meta:
		verbose_name_plural = 'Руководители'
		verbose_name = 'Руководитель'

class Uslugi(models.Model):
	cat_usl = models.ForeignKey(CatUslugi, null=True, on_delete=models.PROTECT, verbose_name='Категория услуги')
	vid_uslugi = ChainedForeignKey(
        VidUslugi,
        chained_field='cat_usl',
        chained_model_field='cat_usl',
        show_all=False,
        auto_choose=True,
        null=True,
        verbose_name='Вид услуги')
	description = models.TextField(verbose_name='Описание услуги')
	documents = models.TextField(verbose_name='Список документов (через ;)')
	price = models.CharField(max_length=50, verbose_name='Стоимость услуги', null=True)
	url_gosuslugi = models.URLField(verbose_name='Адрес госуслуги', null=True)
	url_usl_on_site = models.URLField(verbose_name='Адрес на сайте региона', null=True)

	class Meta:
		verbose_name_plural = 'Услуги'
		verbose_name = 'Услуга'
