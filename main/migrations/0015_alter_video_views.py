# Generated by Django 3.2.4 on 2021-06-05 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_video_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='views',
            field=models.BigIntegerField(default=0, verbose_name='Views'),
        ),
    ]
