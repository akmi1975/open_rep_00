# Generated by Django 2.2.5 on 2019-10-23 10:46

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('rep_test_00', '0008_auto_20191023_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nsp',
            name='rayon',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='region', chained_model_field='region', on_delete=django.db.models.deletion.CASCADE, to='rep_test_00.GorRayon'),
        ),
    ]