# Generated by Django 3.2.8 on 2021-10-18 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Musicapp', '0011_rename_updated_youtube_newly_updated'),
    ]

    operations = [
        migrations.RenameField(
            model_name='youtube',
            old_name='newly_updated',
            new_name='updated',
        ),
    ]
