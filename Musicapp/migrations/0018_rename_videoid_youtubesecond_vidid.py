# Generated by Django 3.2.8 on 2021-10-19 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Musicapp', '0017_rename_updated_youtubesecond_update'),
    ]

    operations = [
        migrations.RenameField(
            model_name='youtubesecond',
            old_name='VideoId',
            new_name='vidId',
        ),
    ]
