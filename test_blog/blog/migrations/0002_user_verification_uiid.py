# Generated by Django 2.0.6 on 2018-06-30 11:46

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='verification_uiid',
            field=models.UUIDField(default=uuid.uuid4, verbose_name='Unique Verification UUID'),
        ),
    ]