# Generated by Django 3.2.8 on 2021-10-18 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Musicapp', '0010_youtube'),
    ]

    operations = [
        migrations.RenameField(
            model_name='youtube',
            old_name='updated',
            new_name='newly_updated',
        ),
    ]
