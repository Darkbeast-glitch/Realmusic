# Generated by Django 3.2.8 on 2021-10-13 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Musicapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shows',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='shows',
            name='venue',
            field=models.CharField(default=1, max_length=200, null=True),
        ),
    ]
