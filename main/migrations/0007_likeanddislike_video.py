# Generated by Django 3.2.4 on 2021-06-04 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_likeanddislike_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='likeanddislike',
            name='video',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='acts', to='main.video', verbose_name='Video'),
            preserve_default=False,
        ),
    ]