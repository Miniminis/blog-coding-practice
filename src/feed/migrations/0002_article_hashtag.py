# Generated by Django 2.1.5 on 2019-01-15 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='hashtag',
            field=models.ManyToManyField(to='feed.HashTag'),
        ),
    ]
