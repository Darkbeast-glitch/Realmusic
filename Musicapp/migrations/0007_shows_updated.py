# Generated by Django 3.2.8 on 2021-10-13 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Musicapp', '0006_remove_shows_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='shows',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
