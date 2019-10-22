# Generated by Django 2.2.5 on 2019-10-22 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rep_test_00', '0002_gorrayon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nsp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('rayon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='rep_test_00.GorRayon')),
                ('region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='rep_test_00.Regions')),
            ],
        ),
    ]
