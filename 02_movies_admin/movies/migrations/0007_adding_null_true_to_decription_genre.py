# Generated by Django 3.2 on 2022-06-23 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_adding_null_true_to_filds_filmwork'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
    ]
