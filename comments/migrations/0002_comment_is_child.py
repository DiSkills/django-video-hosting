# Generated by Django 3.2.4 on 2021-06-05 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='is_child',
            field=models.BooleanField(default=False),
        ),
    ]