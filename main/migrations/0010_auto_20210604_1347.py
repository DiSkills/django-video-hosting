# Generated by Django 3.2.4 on 2021-06-04 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20210604_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dislike',
            name='vote',
            field=models.CharField(max_length=10, verbose_name='Vote'),
        ),
        migrations.AlterField(
            model_name='like',
            name='vote',
            field=models.CharField(max_length=10, verbose_name='Vote'),
        ),
    ]