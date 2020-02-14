# Generated by Django 2.2.6 on 2020-02-14 19:32

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('rep_test_00', '0023_sheff'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatUslugi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование категории')),
            ],
            options={
                'verbose_name': 'Категория услуг',
                'verbose_name_plural': 'Категории услуг',
            },
        ),
        migrations.CreateModel(
            name='VidUslugi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование вида')),
                ('cat_usl', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='rep_test_00.CatUslugi', verbose_name='Категория услуги')),
            ],
            options={
                'verbose_name': 'Вид услуги',
                'verbose_name_plural': 'Виды услуг',
            },
        ),
        migrations.CreateModel(
            name='Uslugi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Описание услуги')),
                ('documents', models.TextField(verbose_name='Список документов (через ;)')),
                ('price', models.CharField(max_length=50, verbose_name='Стоимость услуги')),
                ('url_gosuslugi', models.URLField(verbose_name='Адрес госуслуги')),
                ('cat_uslugi', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='rep_test_00.CatUslugi', verbose_name='Категория услуги')),
                ('vid_uslugi', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='cat_usl', chained_model_field='cat_usl', null=True, on_delete=django.db.models.deletion.CASCADE, to='rep_test_00.VidUslugi', verbose_name='Вид услуги')),
            ],
        ),
        migrations.AddField(
            model_name='org',
            name='cat_uslugi',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='rep_test_00.CatUslugi', verbose_name='Категория услуги'),
        ),
        migrations.AddField(
            model_name='org',
            name='vid_uslugi',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='cat_usl', chained_model_field='cat_usl', null=True, on_delete=django.db.models.deletion.CASCADE, to='rep_test_00.VidUslugi', verbose_name='Вид услуги'),
        ),
    ]