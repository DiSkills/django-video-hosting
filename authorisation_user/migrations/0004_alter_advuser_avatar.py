# Generated by Django 3.2.4 on 2021-06-03 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorisation_user', '0003_advuser_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advuser',
            name='avatar',
            field=models.ImageField(upload_to='', verbose_name='Avatar'),
        ),
    ]
