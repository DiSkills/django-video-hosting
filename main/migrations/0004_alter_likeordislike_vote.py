# Generated by Django 3.2.4 on 2021-06-06 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likeordislike',
            name='vote',
            field=models.CharField(choices=[('like', 'Like'), ('dislike', 'Dislike')], max_length=10, verbose_name='Vote'),
        ),
    ]