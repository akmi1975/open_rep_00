# Generated by Django 2.2.5 on 2019-10-23 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rep_test_00', '0004_auto_20191022_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nsp',
            name='rayon',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='rayons', to='rep_test_00.GorRayon', verbose_name='Район'),
        ),
    ]
