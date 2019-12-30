# Generated by Django 2.2.5 on 2019-12-30 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rep_test_00', '0019_auto_20191205_1453'),
    ]

    operations = [
        migrations.CreateModel(
            name='orgContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adres', models.CharField(max_length=200, verbose_name='Адрес')),
                ('telefone', models.CharField(max_length=50, verbose_name='Телефоны')),
                ('email', models.CharField(max_length=50, verbose_name='e-mail')),
                ('url', models.CharField(max_length=50, verbose_name='Интрнет адрес')),
                ('vremya', models.CharField(max_length=50, verbose_name='Время работы')),
                ('org', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='rep_test_00.Org', verbose_name='Организация')),
            ],
            options={
                'verbose_name': 'Контактная информация',
                'verbose_name_plural': 'Контактная информация',
            },
        ),
    ]
