# Generated by Django 2.0.7 on 2018-07-20 06:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20180717_1153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='user',
        ),
        migrations.AddField(
            model_name='room',
            name='user',
            field=models.ManyToManyField(related_name='rooms', to=settings.AUTH_USER_MODEL),
        ),
    ]