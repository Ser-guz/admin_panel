# Generated by Django 3.2 on 2022-06-15 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_adding_locate_translation'),
    ]

    operations = [
        migrations.AddField(
            model_name='filmwork',
            name='certificate',
            field=models.CharField(blank=True, max_length=512, verbose_name='certificate'),
        ),
        migrations.AddField(
            model_name='filmwork',
            name='file_path',
            field=models.FileField(blank=True, null=True, upload_to='movies/', verbose_name='file'),
        ),
    ]