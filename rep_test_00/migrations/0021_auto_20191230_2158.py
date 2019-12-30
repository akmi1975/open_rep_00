# Generated by Django 2.2.6 on 2019-12-30 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rep_test_00', '0020_orgcontact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orgcontact',
            name='adres',
            field=models.CharField(max_length=200, null=True, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='orgcontact',
            name='email',
            field=models.CharField(max_length=50, null=True, verbose_name='e-mail'),
        ),
        migrations.AlterField(
            model_name='orgcontact',
            name='telefone',
            field=models.CharField(max_length=50, null=True, verbose_name='Телефоны'),
        ),
        migrations.AlterField(
            model_name='orgcontact',
            name='url',
            field=models.CharField(max_length=50, null=True, verbose_name='Интрнет адрес'),
        ),
        migrations.AlterField(
            model_name='orgcontact',
            name='vremya',
            field=models.CharField(max_length=50, null=True, verbose_name='Время работы'),
        ),
    ]
