# Generated by Django 3.2.8 on 2021-10-13 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Musicapp', '0008_rename_shows_show'),
    ]

    operations = [
        migrations.CreateModel(
            name='Show1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('venue', models.CharField(max_length=200)),
                ('Date', models.CharField(max_length=200)),
                ('Time', models.CharField(max_length=6)),
                ('link', models.URLField(max_length=1000)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
