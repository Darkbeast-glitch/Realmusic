# Generated by Django 3.2.8 on 2021-10-18 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Musicapp', '0012_rename_newly_updated_youtube_updated'),
    ]

    operations = [
        migrations.CreateModel(
            name='YouTube2nd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('VideoId', models.CharField(max_length=200)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
