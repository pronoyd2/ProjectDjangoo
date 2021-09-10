# Generated by Django 3.2.6 on 2021-08-28 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='averagerating',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='description',
            field=models.TextField(max_length=5000, null=True),
        ),
    ]