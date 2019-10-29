# Generated by Django 2.2.5 on 2019-10-29 11:50

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('rep_test_00', '0013_auto_20191023_1529'),
    ]

    operations = [
        migrations.CreateModel(
            name='Otrasl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Отрасль',
                'verbose_name_plural': 'Отрасли',
            },
        ),
        migrations.AlterField(
            model_name='nsp',
            name='rayon',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='region', chained_model_field='region', null=True, on_delete=django.db.models.deletion.CASCADE, to='rep_test_00.GorRayon', verbose_name='Район'),
        ),
    ]
