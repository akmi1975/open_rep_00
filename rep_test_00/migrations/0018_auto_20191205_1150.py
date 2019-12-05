# Generated by Django 2.2.5 on 2019-12-05 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rep_test_00', '0017_org'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='org',
            options={'verbose_name': 'Организация', 'verbose_name_plural': 'Организации'},
        ),
        migrations.AddField(
            model_name='org',
            name='name_short',
            field=models.CharField(max_length=300, null=True, verbose_name='Сокращенное наименование'),
        ),
        migrations.AddField(
            model_name='org',
            name='okved',
            field=models.CharField(max_length=8, null=True, verbose_name='ОКВЭД'),
        ),
        migrations.AddField(
            model_name='org',
            name='okved_name',
            field=models.CharField(max_length=500, null=True, verbose_name='ОКВЭД наименование'),
        ),
        migrations.AlterField(
            model_name='org',
            name='name',
            field=models.CharField(max_length=300, verbose_name='Наименование'),
        ),
    ]
