# Generated by Django 3.2 on 2022-06-15 05:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_created_models'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmwork',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='filmwork',
            name='creation_date',
            field=models.DateField(verbose_name='creation_date'),
        ),
        migrations.AlterField(
            model_name='filmwork',
            name='description',
            field=models.TextField(blank=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='filmwork',
            name='genre',
            field=models.ManyToManyField(through='movies.GenreFilmwork', to='movies.Genre', verbose_name='genre'),
        ),
        migrations.AlterField(
            model_name='filmwork',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='modified'),
        ),
        migrations.AlterField(
            model_name='filmwork',
            name='rating',
            field=models.FloatField(default=3.5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='rating'),
        ),
        migrations.AlterField(
            model_name='filmwork',
            name='title',
            field=models.CharField(max_length=255, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='filmwork',
            name='type',
            field=models.CharField(choices=[('movies', 'movies'), ('tv_show', 'tv_show')], default='movies', max_length=15, verbose_name='type'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='description',
            field=models.TextField(blank=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='modified'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=255, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='person',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='person',
            name='full_name',
            field=models.CharField(max_length=30, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='person',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='modified'),
        ),
        migrations.AlterField(
            model_name='personfilmwork',
            name='role',
            field=models.TextField(null=True, verbose_name='role'),
        ),
    ]
